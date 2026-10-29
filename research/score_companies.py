"""Apply the hard gates and scoring from browser-agent-instructions.md to Crunchbase exports.

Usage: python3 -I score_companies.py companies.csv rounds.csv out_dir

Deviations from the instructions, forced by what the exports contain:
- Actively Hiring is almost always blank, and the rounds export only covers recent rounds,
  so the hiring and valuation step-up signals are dropped and their weight redistributed.
- IPO Prediction Tier cannot be exported, so the liquidity signal uses revenue alone.
- Without a known valuation, total funding >= $2B is treated as "likely valued above $10B".
"""
import csv
import sys
from datetime import date
from pathlib import Path

TODAY = date(2026, 10, 29)
LAYOFF_CUTOFF = "2025-11-01"
MAX_VALUATION = 10e9
LIKELY_OVER_MAX_TOTAL_FUNDING = 2e9
MIN_VISITS_FOR_GROWTH = 10_000
TIER = {"Series D": 1.0, "Series E": 1.0, "Series F": 1.0, "Series C": 0.85}
WEIGHTS = {
    "web_momentum": 0.25,
    "trend": 0.15,
    "funding_pace": 0.20,
    "room_to_grow": 0.15,
    "revenue": 0.15,
    "investors": 0.10,
}
REVENUE_SCORE = {
    "$1B to $10B": 1.0, "$10B+": 1.0, "$500M to $1B": 1.0, "$100M to $500M": 1.0,
    "$50M to $100M": 0.6, "$10M to $50M": 0.3, "$1M to $10M": 0.1, "Less than $1M": 0.0,
}
TOP_INVESTORS = [
    "sequoia capital", "andreessen horowitz", "benchmark", "accel", "founders fund",
    "lightspeed venture partners", "index ventures", "greylock", "kleiner perkins",
    "general catalyst", "thrive capital", "coatue", "iconiq", "insight partners",
    "khosla ventures", "redpoint", "bessemer venture partners", "ivp", "tiger global",
    "y combinator",
]


def num(s):
    s = (s or "").replace(",", "").replace("%", "").strip()
    return float(s) if s else None


def percentiles(values):
    """Percentile rank (0-1) of each value among the non-blank ones; blanks become 0.5."""
    known = sorted(v for v in values if v is not None)
    if len(known) < 2:
        return [0.5] * len(values)
    out = []
    for v in values:
        if v is None:
            out.append(0.5)
        else:
            below = sum(1 for k in known if k < v)
            equal = sum(1 for k in known if k == v)
            out.append((below + (equal - 1) / 2) / (len(known) - 1))
    return out


def latest_valuations(rounds):
    latest = {}
    for r in rounds:
        val = num(r["Post-Money Valuation (in USD)"])
        key = r["Organization Name URL"]
        if val and (key not in latest or r["Announced Date"] > latest[key][1]):
            latest[key] = (val, r["Announced Date"], r["Funding Type"])
    return latest


def room_to_grow(valuation):
    if valuation is None:
        return 0.5
    if valuation < 300e6:
        return 0.6
    if valuation <= 3e9:
        return 1.0
    return 0.5


def main(companies_path, rounds_path, out_dir):
    companies = list(csv.DictReader(open(companies_path, encoding="utf-8-sig")))
    valuations = latest_valuations(csv.DictReader(open(rounds_path, encoding="utf-8-sig")))

    for c in companies:
        val = valuations.get(c["Organization Name URL"])
        c["valuation"], c["valuation_date"] = (val[0], val[1]) if val else (None, "")
        total = num(c["Total Funding Amount (in USD)"])
        reasons = []
        if c["Last Layoff Mention Date"] >= LAYOFF_CUTOFF:
            reasons.append(f"layoff {c['Last Layoff Mention Date']}")
        if c["valuation"] and c["valuation"] > MAX_VALUATION:
            reasons.append(f"valuation ${c['valuation'] / 1e9:.1f}B > $10B")
        elif c["valuation"] is None and total and total >= LIKELY_OVER_MAX_TOTAL_FUNDING:
            reasons.append(f"raised ${total / 1e9:.1f}B, likely valued > $10B (verify)")
        c["excluded"] = "; ".join(reasons)

    kept = [c for c in companies if not c["excluded"]]

    growth, ratio = [], []
    for c in kept:
        visits = num(c["Monthly Visits"])
        avg6 = num(c["Average Visits (6 months)"])
        enough = visits is not None and visits >= MIN_VISITS_FOR_GROWTH
        growth.append(num(c["Monthly Visits Growth"]) if enough else None)
        ratio.append(visits / avg6 if enough and avg6 else None)
    web = [(a + b) / 2 for a, b in zip(percentiles(growth), percentiles(ratio))]

    trend = percentiles([num(c["Trend Score (90 Days)"]) for c in kept])

    pace_raw = []
    for c in kept:
        founded = date.fromisoformat(c["Founded Date"]) if c["Founded Date"] else None
        rounds = num(c["Number of Funding Rounds"])
        years = max((TODAY - founded).days / 365.25, 1.0) if founded else None
        pace_raw.append(rounds / years if rounds and years else None)
    pace = percentiles(pace_raw)

    for i, c in enumerate(kept):
        investors = f"{c['Top 5 Investors']}, {c['Lead Investors']}".lower()
        signals = {
            "web_momentum": web[i],
            "trend": trend[i],
            "funding_pace": pace[i],
            "room_to_grow": room_to_grow(c["valuation"]),
            "revenue": REVENUE_SCORE.get(c["Estimated Revenue Range"], 0.5),
            "investors": 1.0 if any(n in investors for n in TOP_INVESTORS) else 0.0,
        }
        c.update({k: round(v, 3) for k, v in signals.items()})
        c["tier"] = 1 if TIER[c["Last Funding Type"]] == 1.0 else 2
        c["final_score"] = round(
            sum(WEIGHTS[k] * v for k, v in signals.items()) * TIER[c["Last Funding Type"]], 4
        )

    kept.sort(key=lambda c: c["final_score"], reverse=True)
    for rank, c in enumerate(kept, 1):
        c["rank"] = rank

    cols = [
        "rank", "Organization Name", "Organization Name URL", "tier", "final_score",
        "Last Funding Type", "Last Funding Date", "valuation", "valuation_date",
        "Total Funding Amount (in USD)", "Estimated Revenue Range", "Number of Employees",
        "Headquarters Location", "Industries", *WEIGHTS, "Top 5 Investors", "Description",
    ]
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    with open(out / "scored.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(kept)
    with open(out / "excluded.csv", "w", newline="") as f:
        w = csv.DictWriter(
            f, fieldnames=["Organization Name", "Organization Name URL", "excluded"],
            extrasaction="ignore",
        )
        w.writeheader()
        w.writerows(c for c in companies if c["excluded"])
    print(f"{len(companies)} companies, {len(companies) - len(kept)} excluded, {len(kept)} scored")


if __name__ == "__main__":
    main(*sys.argv[1:4])
