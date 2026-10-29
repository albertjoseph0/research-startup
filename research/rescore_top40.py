"""Re-score the top 40 after the Phase 5 profile check.

Usage: python3 -I rescore_top40.py scored.csv top_40.csv out_dir

Uses the checked valuations to recompute room to grow, adds a valuation-momentum signal
(annualised growth from the previous valuation), drops companies now known to be above
$10B, and applies penalties for red flags found in the hand check.
"""
import csv
import re
import sys
from datetime import date
from pathlib import Path

from score_companies import MAX_VALUATION, TIER, WEIGHTS, percentiles, room_to_grow

MOMENTUM_WEIGHT = 0.15
# Hand-check red flags, as multipliers on the score. Keyed by Crunchbase company name.
RED_FLAGS = {
    "H1.co": (0.85, "down round: $1.0B Series D after a $1.1B valuation"),
    "Turing": (0.85, "2025 Series E at $2.2B is below the 2021 $4B convertible-note valuation"),
    "Commure": (0.95, "ended AI referral payments to customers (STAT, Aug 2026)"),
    "EliseAI": (0.95, "RealPage halted its EliseAI integration (Oct 2026)"),
    "Also": (0.95, "e-bike deliveries months late, reported order cancellations"),
}


def money(s):
    m = re.search(r"\$([\d.]+)\s*([MB])", s or "")
    if not m:
        return None
    return float(m.group(1)) * (1e9 if m.group(2) == "B" else 1e6)


def first_date(s):
    m = re.search(r"\d{4}-\d{2}-\d{2}", s or "")
    return date.fromisoformat(m.group(0)) if m else None


def main(scored_path, top40_path, out_dir):
    scored = {r["Organization Name"]: r for r in csv.DictReader(open(scored_path))}
    rows = []
    for t in csv.DictReader(open(top40_path, encoding="utf-8-sig")):
        name = t["company"].split(" - ")[0].strip()
        base = scored[name]
        val, prev = money(t["latest_valuation"]), money(t["previous_valuation"])
        val_date, prev_date = first_date(t["valuation_date"]), first_date(t["previous_valuation"])
        momentum = None
        if val and prev and val_date and prev_date:
            years = max((val_date - prev_date).days / 365.25, 0.25)
            momentum = (val / prev) ** (1 / years)
        rows.append({**base, **t, "name": name, "checked_valuation": val, "momentum_raw": momentum})

    kept = [r for r in rows if not (r["checked_valuation"] and r["checked_valuation"] > MAX_VALUATION)]
    momentum = percentiles([r["momentum_raw"] for r in kept])
    for r, m in zip(kept, momentum):
        r["room_to_grow"] = room_to_grow(r["checked_valuation"])
        r["valuation_momentum"] = round(m, 3)
        weighted = (1 - MOMENTUM_WEIGHT) * sum(w * float(r[k]) for k, w in WEIGHTS.items())
        weighted += MOMENTUM_WEIGHT * m
        penalty, flag = RED_FLAGS.get(r["name"], (1.0, ""))
        r["red_flag_applied"] = flag
        r["new_score"] = round(weighted * TIER[r["Last Funding Type"]] * penalty, 4)
    kept.sort(key=lambda r: r["new_score"], reverse=True)

    cols = [
        "new_rank", "old_rank", "name", "Organization Name URL", "tier", "new_score",
        "latest_valuation", "valuation_date", "annualised_valuation_growth", "5x_check",
        "red_flag_applied", "Last Funding Type", "Number of Employees",
        "Estimated Revenue Range", "why_it_could_be_very_large", "red_flags",
    ]
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    with open(out / "top_40_rescored.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for i, r in enumerate(kept, 1):
            m = r["momentum_raw"]
            w.writerow({
                **r, "new_rank": i, "old_rank": r["rank"],
                "annualised_valuation_growth": f"{m:.2f}x" if m else "",
            })
    dropped = [r["name"] for r in rows if r not in kept]
    print(f"{len(kept)} re-scored, dropped over $10B: {', '.join(dropped)}")


if __name__ == "__main__":
    main(*sys.argv[1:4])
