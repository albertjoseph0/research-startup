"""Score a Crunchbase company export using the rules in browser-agent-instructions.md.

Usage: python3 score_all.py COMPANIES.csv ROUNDS.csv PROFILE_CHECKS.csv OUT.csv
                            [JOB1_HIRING.csv JOB2_REVENUE.csv JOB3_LIQUIDITY.csv]

Any CSV argument except PROFILE_CHECKS and OUT may be several comma-separated files.

The optional job files (browser-agent-brute-force.md) add hiring, revenue-multiple and
early-cash signals and exclude companies the research found acquired or going public.
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


def previous_round_valuation(rounds):
    """Valuation of the latest earlier round with a different round type, so that
    tranches of the same round are not mistaken for a step-up."""
    latest = rounds.iloc[-1]
    earlier = rounds.iloc[:-1]
    earlier = earlier[earlier["Funding Type"] != latest["Funding Type"]]
    return earlier["Post-Money Valuation (in USD)"].iloc[-1] if len(earlier) else None


def read_all(paths):
    """Read one CSV, or several comma-separated CSVs with the same columns."""
    return pd.concat([pd.read_csv(p) for p in paths.split(",")], ignore_index=True)


def fragility_flags(s, hand):
    """Reasons a company's equity is fragile: upside capped or downside added."""
    funding_ratio = s["total_funding"] / s["valuation"]
    layoff = s["Last Layoff Mention Date"].fillna("")
    last_round = pd.to_datetime(s["Last Funding Date"], errors="coerce", format="mixed")
    hand_down = s["Organization Name"].map(
        hand["red_flags"].str.contains("down round", case=False, na=False)).eq(True)
    flags = {
        "raised half or more of valuation": funding_ratio >= 0.5,
        "down round": (s["step_up"] < 1) | hand_down,
        "layoff in last 2 years": layoff >= (TODAY - pd.Timedelta(days=730)).strftime("%Y-%m-%d"),
        "no new round in 2 years": last_round < TODAY - pd.Timedelta(days=730),
        "sale talks": s.get("sale_talks", pd.Series(False, index=s.index)).eq(True),
    }
    return pd.Series(["; ".join(k for k, m in flags.items() if m[i]) for i in s.index], index=s.index)


def robustness(s, weights, runs=2000, seed=0):
    """Share of runs, with each weight scaled by a random factor in [0.5, 1.5], in which
    each company lands in the top 25 and the top 50."""
    names = list(weights)
    x = s[names].fillna(0.5).to_numpy()
    base = np.array([weights[k] for k in names])
    rng = np.random.default_rng(seed)
    top25, top50 = np.zeros(len(s)), np.zeros(len(s))
    for _ in range(runs):
        w = base * rng.uniform(0.5, 1.5, len(base))
        order = np.argsort(-(x @ w))
        top25[order[:25]] += 1
        top50[order[:50]] += 1
    return top25 / runs, top50 / runs


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


# Crunchbase API codes and the labels shown on profile pages.
ESTIMATED = {"c200_estimated": True, "Estimated": True, "c100_confirmed": False, "Confirmed": False}
EMPLOYEE_MIDPOINT = {"101-250": 175, "251-500": 375, "501-1000": 750, "1001-5000": 3000}
REPORTED_REVENUE = {"ARR", "annual revenue", "run-rate", "revenue"}
# Brute-force research (job3_liquidity.csv) facts that end the private-company bet.
EXIT_SIGNAL = r"^ACQUIRED by|^Definitive agreement.*to acquire|^MERGED with|Chapter 11"
SALE_TALKS = r"M&A talks|sale talks|exploring a sale|in talks to be acquired|hired a banker"
# Score weights with research inputs. Robustness checks vary each weight by +/-50%.
WEIGHTS = {"web": 0.15, "hiring": 0.10, "trend": 0.05, "pace": 0.10, "step": 0.10,
           "room": 0.25, "liquidity": 0.15, "revenue": 0.05, "investors": 0.05}
AI_INDUSTRIES = r"Artificial Intelligence|Machine Learning|Generative AI|Agentic AI|Foundational AI"


def load_research(job1_path, job2_path, job3_path):
    """Per-company research signals keyed by Crunchbase URL."""
    frames = [read_all(p) for p in (job1_path, job2_path, job3_path)]
    # Some job rows lost their URL; recover it from another job's row for the same company.
    urls = pd.concat(frames).dropna(subset=["crunchbase_url"]).drop_duplicates("company")
    urls = urls.set_index("company")["crunchbase_url"]

    def keyed(df):
        df = df.assign(crunchbase_url=df["crunchbase_url"].fillna(df["company"].map(urls)))
        # Rows found outside the Crunchbase universe (Job 7) still have no URL and are skipped.
        return df.dropna(subset=["crunchbase_url"]).drop_duplicates("crunchbase_url").set_index("crunchbase_url")
    j1, j2, j3 = (keyed(df) for df in frames)
    out = pd.DataFrame(index=j1.index.union(j2.index).union(j3.index))

    out["open_roles"] = pd.to_numeric(j1["open_roles_now"], errors="coerce")
    out["target_roles"] = pd.to_numeric(j1["open_roles_target_role_now"], errors="coerce")
    past = pd.to_numeric(j1["open_roles_12mo_ago"], errors="coerce").fillna(
        pd.to_numeric(j1["open_roles_6mo_ago"], errors="coerce"))
    out["hiring_growth"] = (out["open_roles"] + 1) / (past + 1)

    revenue = pd.to_numeric(j2["revenue_usd"], errors="coerce")
    out["revenue_usd"] = revenue.where(j2["revenue_type"].isin(REPORTED_REVENUE))

    details = j3["tender_offer_details"].fillna("")
    has_tender = ~j3["tender_offer_date"].fillna("None found").str.startswith("None found")
    investors_only = details.str.contains("not employee", case=False)
    unclear = details.str.contains("not stated|unverified", case=False)
    out["tender"] = pd.Series(np.select(
        [has_tender & ~investors_only & ~unclear, has_tender & ~investors_only & unclear],
        ["employee tender", "tender, eligibility unclear"], ""), index=j3.index)
    ipo = j3["ipo_signal"].fillna("")
    out["ipo_filed"] = ipo.str.contains("filed an S-1", case=False)
    exit_reason = np.select(
        [j3["acquisition_signal"].fillna("").str.contains(EXIT_SIGNAL, case=False),
         ipo.str.contains("IPO priced", case=False),
         ipo.str.contains(r"\bSPAC\b")],
        ["acquired, merged or bankrupt", "now public", "going public via SPAC"], "")
    out["exit_reason"] = pd.Series(exit_reason, index=j3.index)
    out["sale_talks"] = j3["acquisition_signal"].fillna("").str.contains(SALE_TALKS, case=False)
    return out


def main(companies_path, rounds_path, top40_path, out_path, job1=None, job2=None, job3=None):
    c = read_all(companies_path)
    research = load_research(job1, job2, job3) if job1 else pd.DataFrame()
    for col in research:
        c[col] = c["Organization Name URL"].map(research[col])
    r = read_all(rounds_path).drop_duplicates("Transaction Name URL")
    t = pd.read_csv(top40_path)
    t["name"] = t["company"].str.split(" - ").str[0]

    # Latest valuation: hand-checked top-40 value first, then the rounds export.
    r = r.dropna(subset=["Post-Money Valuation (in USD)"]).sort_values("Announced Date")
    if "Valuation Source" not in r:
        r["Valuation Source"] = None
    last_round = r.groupby("Organization Name").last()
    c["valuation"] = c["Organization Name"].map(last_round["Post-Money Valuation (in USD)"])
    c["valuation_source"] = c["valuation"].notna().map({True: "rounds export", False: ""})
    # Blank when the source does not say (the browser rounds export has no such field).
    c["valuation_estimated"] = c["Organization Name"].map(
        last_round["Valuation Source"].map(ESTIMATED))
    round_prev = r.groupby("Organization Name").apply(previous_round_valuation)
    hand = t.set_index("name")
    # The fact-check pass marks figures it could not confirm; treat those as unknown.
    hand_val = hand["latest_valuation"].map(parse_money).mask(
        hand["latest_valuation"].str.contains("UNVERIFIABLE", na=False))
    hand_prev = hand["previous_valuation"].map(prior_valuation)
    in_hand = c["Organization Name"].isin(hand_val.dropna().index)
    c.loc[in_hand, "valuation"] = c.loc[in_hand, "Organization Name"].map(hand_val)
    c.loc[in_hand, "valuation_source"] = "top-40 profile check"
    # Hand checks record whether Crunchbase marks the round Confirmed or Estimated;
    # they also cover valuations taken from the rounds export, which has no such field.
    hand_estimated = (hand["valuation_date"].str.contains("Estimated", na=False)
                      | hand["latest_valuation"].str.contains("UNVERIFIABLE", na=False))
    hand_confirmed = hand["valuation_date"].str.contains("Confirmed", na=False) & ~hand_estimated
    checked = c["Organization Name"].isin(hand.index[hand_estimated | hand_confirmed])
    c.loc[checked, "valuation_estimated"] = c.loc[checked, "Organization Name"].map(hand_estimated)
    prev = c["Organization Name"].map(hand_prev).fillna(c["Organization Name"].map(round_prev))
    c["step_up"] = c["valuation"] / prev

    c["total_funding"] = num(c["Total Funding Amount (in USD)"])

    # Hard gates.
    c["excluded"] = ""
    # The original export applied these filters; rows added from other sources may not meet them.
    employees = c["Number of Employees"].fillna("")
    c.loc[employees.isin(["1-10", "11-50", "51-100"]), "excluded"] = "under 101 employees"
    c.loc[~c["Headquarters Location"].fillna("").str.endswith("United States"), "excluded"] = "not US-headquartered"
    c.loc[c["IPO Status"].fillna("") != "Private", "excluded"] = "not private"
    c.loc[c["Operating Status"].fillna("") != "Active", "excluded"] = "not active"
    c.loc[c["Last Layoff Mention Date"].fillna("") >= LAYOFF_CUTOFF, "excluded"] = "layoff since " + LAYOFF_CUTOFF
    c.loc[(c["excluded"] == "") & (c["valuation"] > MAX_VALUATION), "excluded"] = "valuation over $10B"
    ended = hand["red_flags"].str.contains(ENDED, case=False, na=False)
    for name in ended[ended].index:
        c.loc[(c["excluded"] == "") & (c["Organization Name"] == name), "excluded"] = "acquired or bankrupt"
    for name, reason in KNOWN_OVER_10B.items():
        c.loc[(c["excluded"] == "") & (c["Organization Name"] == name), "excluded"] = reason
    if "exit_reason" in c:
        research_exit = (c["excluded"] == "") & c["exit_reason"].fillna("").ne("")
        c.loc[research_exit, "excluded"] = c.loc[research_exit, "exit_reason"]
    c["check_valuation"] = c["valuation"].isna() & (c["total_funding"] > 1.5e9)

    s = c[c["excluded"] == ""].copy()
    visits, avg6 = num(s["Monthly Visits"]), num(s["Average Visits (6 months)"])
    s["web"] = (pct(num(s["Monthly Visits Growth"])) + pct(visits / avg6)) / 2
    s["trend"] = pct(num(s["Trend Score (90 Days)"]))
    years = (TODAY - pd.to_datetime(s["Founded Date"], errors="coerce", format="mixed")).dt.days / 365.25
    s["pace"] = pct(num(s["Number of Funding Rounds"]) / years.clip(lower=1))
    s["step"] = pct(s["step_up"])
    s["room"] = s["valuation"].map(room_to_grow)
    # A Crunchbase model estimate is weaker evidence than a reported round: halve its pull.
    estimated = s["valuation_estimated"].eq(True)
    s.loc[estimated, "room"] = (s.loc[estimated, "room"] + 0.5) / 2
    big_revenue = s["Estimated Revenue Range"].isin(["$100M to $500M", "$500M to $1B", "$1B to $10B"])
    s["liquidity"] = (0.5 + 0.2 * big_revenue).clip(upper=1.0)  # IPO tier not exported: neutral 0.5
    investors = s["Top 5 Investors"].fillna("") + ", " + s["Lead Investors"].fillna("")
    s["investors"] = investors.map(lambda x: float(any(i in x for i in TOP_INVESTORS)))

    if research.empty:
        # Entry price, not round name, sets the preference: round valuations are 3-5x higher
        # than in 2015-19, so "Series D/E" no longer means a ~$500M company.
        s["final_score"] = (0.20 * s["web"] + 0.10 * s["trend"] + 0.15 * s["pace"] + 0.10 * s["step"]
                            + 0.25 * s["room"] + 0.10 * s["liquidity"] + 0.10 * s["investors"])
    else:
        # Early cash: a proven employee tender or a filed S-1 is direct evidence of liquidity.
        tender = s["tender"].fillna("")
        s.loc[tender.eq("tender, eligibility unclear"), "liquidity"] = s["liquidity"].clip(lower=0.8)
        s.loc[tender.eq("employee tender") | s["ipo_filed"].eq(True), "liquidity"] = 1.0
        intensity = s["open_roles"] / s["Number of Employees"].map(EMPLOYEE_MIDPOINT)
        growth = s["hiring_growth"].clip(upper=10)
        s["hiring"] = pd.concat([pct(intensity).where(intensity.notna()),
                                 pct(growth).where(growth.notna())], axis=1).mean(axis=1).fillna(0.5)
        s["revenue_multiple"] = s["valuation"] / s["revenue_usd"]
        s["revenue"] = pct(-s["revenue_multiple"])  # cheaper per dollar of revenue is better
        s["final_score"] = sum(w * s[k] for k, w in WEIGHTS.items())
    s["price_band"] = s["valuation"].map(price_band)
    s["sector"] = s["Industries"].fillna("").str.contains(AI_INDUSTRIES).map({True: "AI", False: "non-AI"})

    # Remove fragility rather than trust small score differences: flag exposures that
    # cut off the upside or add downside, then group the rest into tiers by how stable
    # their position is when the weights change.
    s["fragility"] = fragility_flags(s, hand)
    s = s.sort_values("final_score", ascending=False)
    s.insert(0, "rank", range(1, len(s) + 1))
    s["top25_share"] = s["top50_share"] = np.nan
    if not research.empty:
        pool = s["fragility"] == ""
        top25, top50 = robustness(s[pool], WEIGHTS)
        s.loc[pool, "top25_share"], s.loc[pool, "top50_share"] = top25, top50
    s["tier"] = np.select(
        [s["fragility"] != "", s["top25_share"] >= 0.8, s["top50_share"] >= 0.5],
        ["F - fragile", "A - core pool", "B - wider pool"], "C - rest")
    s["agent_top40_rank"] = s["Organization Name"].map(hand["rank"])
    for col in ["red_flags", "5x_check", "why_it_could_be_very_large"]:
        s[col] = s["Organization Name"].map(hand[col])
    cols = ["tier", "rank", "Organization Name", "Organization Name URL", "fragility", "top25_share",
            "top50_share", "sector", "price_band", "final_score",
            "valuation", "valuation_source", "valuation_estimated", "step_up", "check_valuation", "Last Funding Type",
            "Last Funding Date", "Number of Employees", "Estimated Revenue Range",
            "Monthly Visits Growth", "Trend Score (90 Days)", "web", "trend", "pace", "step",
            "room", "liquidity", "investors", "agent_top40_rank", "red_flags", "5x_check", "why_it_could_be_very_large", "Industries",
            "Description"]
    if not research.empty:
        cols[cols.index("investors") + 1:cols.index("investors") + 1] = [
            "hiring", "revenue", "open_roles", "target_roles", "hiring_growth", "revenue_usd",
            "revenue_multiple", "tender", "ipo_filed"]
    s = s.sort_values(["tier", "rank"])
    s[cols].to_csv(out_path, index=False)
    excluded = c[c["excluded"] != ""][["Organization Name", "excluded", "valuation"]]
    excluded.to_csv(out_path.replace(".csv", "_excluded.csv"), index=False)
    print(f"scored {len(s)}, excluded {len(excluded)}")


if __name__ == "__main__":
    main(*sys.argv[1:8])
