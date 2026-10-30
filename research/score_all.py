"""Score a Crunchbase company export using the rules in browser-agent-instructions.md.

Usage: python3 score_all.py COMPANIES.csv ROUNDS.csv[,ROUNDS2.csv...] PROFILE_CHECKS.csv OUT.csv
"""
import re
import sys

import numpy as np
import pandas as pd

TOP_INVESTORS = [
    "Sequoia Capital", "Andreessen Horowitz", "Benchmark", "Accel", "Founders Fund",
    "Lightspeed Venture Partners", "Index Ventures", "Greylock", "Kleiner Perkins",
    "General Catalyst", "Thrive Capital", "Coatue", "ICONIQ", "Insight Partners",
    "Khosla Ventures", "Redpoint", "Bessemer Venture Partners", "IVP", "Tiger Global",
    "Y Combinator",
]
LAYOFF_CUTOFF = "2025-11-01"
MAX_VALUATION = 10e9
TODAY = pd.Timestamp("2026-10-30")
# Red flags that end standalone upside.
ENDED = r"acquired by|acquisition by|Chapter 11|bankruptcy"
# Valuations missing from the exports but widely reported above the $10B gate.
KNOWN_OVER_10B = {
    "Anysphere (Cursor)": "valuation over $10B ($29.3B, Nov 2025 reporting)",
    "Applied Intuition": "valuation over $10B ($15B, Jun 2025 reporting)",
}


def num(series):
    return pd.to_numeric(series.astype(str).str.replace(r"[,%$]", "", regex=True), errors="coerce")


def parse_money(text):
    """'$2.2B' / '$650M' / 'Over $2B' -> float USD; None if no figure."""
    m = re.search(r"\$([\d.]+)\s*([BM])", str(text))
    if not m:
        return None
    return float(m.group(1)) * (1e9 if m.group(2) == "B" else 1e6)


def prior_valuation(text):
    """Previous separately priced round. When the agent marked the listed prior as a
    tranche of the same round, use the round it names as the last separate one."""
    text = str(text)
    marker = "last genuinely separate"
    if marker in text:
        text = text[text.index(marker):]
    elif "NOT a separate" in text:
        return None
    if "UNVERIFIABLE" in text.split(" - step-up")[0]:
        return None
    return parse_money(text)


def pct(series):
    """Percentile rank among scored companies; blanks are neutral (0.5)."""
    return series.rank(pct=True).fillna(0.5)


# Price range where a 5x gain is most reachable. The 2015-19 Series D/E cohorts that most
# often turned 5x into cash within 4 years joined at median valuations of $327M and $584M.
SWEET_SPOT = (300e6, 1.5e9)


def room_to_grow(v):
    """1.0 inside the sweet spot, falling on a log scale outside it; unknown is neutral."""
    if pd.isna(v):
        return 0.5
    low, high = SWEET_SPOT
    if v < low:  # cheaper but riskier: 0.5 at $100M
        return float(np.clip(1 - 0.5 * np.log(low / v) / np.log(3), 0.3, 1.0))
    if v <= high:
        return 1.0
    return float(np.clip(1 - 0.9 * np.log(v / high) / np.log(MAX_VALUATION / high), 0.1, 1.0))


def price_band(v):
    if pd.isna(v):
        return "unknown"
    for limit, label in [(300e6, "under $300M"), (1.5e9, "$300M-$1.5B"), (3e9, "$1.5B-$3B")]:
        if v < limit:
            return label
    return "$3B-$10B"


def main(companies_path, rounds_path, top40_path, out_path):
    c = pd.read_csv(companies_path)
    r = pd.concat([pd.read_csv(p) for p in rounds_path.split(",")]).drop_duplicates("Transaction Name URL")
    t = pd.read_csv(top40_path)
    t["name"] = t["company"].str.split(" - ").str[0]

    # Latest valuation: hand-checked top-40 value first, then the rounds export.
    r = r.sort_values("Announced Date")
    last_round = r.groupby("Organization Name").last()
    c["valuation"] = c["Organization Name"].map(last_round["Post-Money Valuation (in USD)"])
    c["valuation_source"] = c["valuation"].notna().map({True: "rounds export", False: ""})
    hand = t.set_index("name")
    # The fact-check pass marks figures it could not confirm; treat those as unknown.
    hand_val = hand["latest_valuation"].map(parse_money).mask(
        hand["latest_valuation"].str.contains("UNVERIFIABLE", na=False))
    hand_prev = hand["previous_valuation"].map(prior_valuation)
    in_hand = c["Organization Name"].isin(hand_val.dropna().index)
    c.loc[in_hand, "valuation"] = c.loc[in_hand, "Organization Name"].map(hand_val)
    c.loc[in_hand, "valuation_source"] = "top-40 profile check"
    c["step_up"] = c["valuation"] / c["Organization Name"].map(hand_prev)

    c["total_funding"] = num(c["Total Funding Amount (in USD)"])

    # Hard gates.
    c["excluded"] = ""
    c.loc[c["Last Layoff Mention Date"].fillna("") >= LAYOFF_CUTOFF, "excluded"] = "layoff since " + LAYOFF_CUTOFF
    c.loc[(c["excluded"] == "") & (c["valuation"] > MAX_VALUATION), "excluded"] = "valuation over $10B"
    ended = hand["red_flags"].str.contains(ENDED, case=False, na=False)
    for name in ended[ended].index:
        c.loc[(c["excluded"] == "") & (c["Organization Name"] == name), "excluded"] = "acquired or bankrupt"
    for name, reason in KNOWN_OVER_10B.items():
        c.loc[(c["excluded"] == "") & (c["Organization Name"] == name), "excluded"] = reason
    c["check_valuation"] = c["valuation"].isna() & (c["total_funding"] > 1.5e9)

    s = c[c["excluded"] == ""].copy()
    visits, avg6 = num(s["Monthly Visits"]), num(s["Average Visits (6 months)"])
    s["web"] = (pct(num(s["Monthly Visits Growth"])) + pct(visits / avg6)) / 2
    s["trend"] = pct(num(s["Trend Score (90 Days)"]))
    years = (TODAY - pd.to_datetime(s["Founded Date"], errors="coerce")).dt.days / 365.25
    s["pace"] = pct(num(s["Number of Funding Rounds"]) / years.clip(lower=1))
    s["step"] = pct(s["step_up"])
    s["room"] = s["valuation"].map(room_to_grow)
    big_revenue = s["Estimated Revenue Range"].isin(["$100M to $500M", "$500M to $1B", "$1B to $10B"])
    s["liquidity"] = (0.5 + 0.2 * big_revenue).clip(upper=1.0)  # IPO tier not exported: neutral 0.5
    investors = s["Top 5 Investors"].fillna("") + ", " + s["Lead Investors"].fillna("")
    s["investors"] = investors.map(lambda x: float(any(i in x for i in TOP_INVESTORS)))

    # Entry price, not round name, sets the preference: round valuations are 3-5x higher
    # than in 2015-19, so "Series D/E" no longer means a ~$500M company.
    s["final_score"] = (0.20 * s["web"] + 0.10 * s["trend"] + 0.15 * s["pace"] + 0.10 * s["step"]
                        + 0.25 * s["room"] + 0.10 * s["liquidity"] + 0.10 * s["investors"])
    s["price_band"] = s["valuation"].map(price_band)

    s = s.sort_values("final_score", ascending=False)
    s.insert(0, "rank", range(1, len(s) + 1))
    s["agent_top40_rank"] = s["Organization Name"].map(hand["rank"])
    for col in ["red_flags", "5x_check", "why_it_could_be_very_large"]:
        s[col] = s["Organization Name"].map(hand[col])
    cols = ["rank", "Organization Name", "Organization Name URL", "price_band", "final_score",
            "valuation", "valuation_source", "step_up", "check_valuation", "Last Funding Type",
            "Last Funding Date", "Number of Employees", "Estimated Revenue Range",
            "Monthly Visits Growth", "Trend Score (90 Days)", "web", "trend", "pace", "step",
            "room", "liquidity", "investors", "agent_top40_rank", "red_flags", "5x_check", "why_it_could_be_very_large", "Industries",
            "Description"]
    s[cols].to_csv(out_path, index=False)
    excluded = c[c["excluded"] != ""][["Organization Name", "excluded", "valuation"]]
    excluded.to_csv(out_path.replace(".csv", "_excluded.csv"), index=False)
    print(f"scored {len(s)}, excluded {len(excluded)}")


if __name__ == "__main__":
    main(*sys.argv[1:5])
