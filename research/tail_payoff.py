"""Expected payoff ("vanilla") view of threshold counts, after Taleb, Statistical Consequences
of Fat Tails, ch. 11 and 17: compare groups by what a grant is worth, not by the chance of
crossing one threshold, because two groups can rank one way on P(>=5x) and the other way on
payoff when their tails differ.

Usage: python3 tail_payoff.py COUNTS.csv [--from 2] [--caps 100,300,1000] [--alphas 1.1,1.3,1.5]

COUNTS.csv columns: group, n, threshold, count (as for tail_analysis.py).

For each group it estimates V = integral from K to H of P(X > x) dx: the expected cash payoff
above K times the grant's value, per $1 of grant, counting only exits above K. Between observed
thresholds the survival curve is interpolated linearly on log-log axes; above the last observed
threshold it follows a power law with each tail exponent in --alphas, up to the cap H.
The cap stands in for the bounded support behind Taleb's shadow mean: no exit can exceed a
finite company value, so the integral stays finite even when alpha is near or below 1.
The result is sensitive to H whenever alpha is near 1, which is itself the main finding.
"""
import argparse

import numpy as np
import pandas as pd


def payoff(thresholds, survival, k, cap, alpha):
    t, s = np.asarray(thresholds, float), np.asarray(survival, float)
    keep = (t >= k) & (s > 0)
    t, s = t[keep], s[keep]
    total = 0.0
    for (x0, s0), (x1, s1) in zip(zip(t[:-1], s[:-1]), zip(t[1:], s[1:])):
        a = -np.log(s1 / s0) / np.log(x1 / x0)  # local slope on log-log axes
        total += s0 * x0 ** a * (np.log(x1 / x0) if np.isclose(a, 1) else (x1 ** (1 - a) - x0 ** (1 - a)) / (1 - a))
    x0, s0 = t[-1], s[-1]
    if cap > x0:
        a = alpha
        total += s0 * x0 ** a * (np.log(cap / x0) if np.isclose(a, 1) else (cap ** (1 - a) - x0 ** (1 - a)) / (1 - a))
    return total


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("counts")
    ap.add_argument("--from", dest="k", type=float, default=2.0)
    ap.add_argument("--caps", default="100,300,1000")
    ap.add_argument("--alphas", default="1.1,1.3,1.5")
    args = ap.parse_args()
    caps = [float(c) for c in args.caps.split(",")]
    alphas = [float(a) for a in args.alphas.split(",")]
    d = pd.read_csv(args.counts)
    rows = []
    for g, x in d.groupby("group", sort=False):
        x = x.sort_values("threshold")
        surv = x["count"] / x["n"]
        p5 = surv[x.threshold == 5].iloc[0] if (x.threshold == 5).any() else np.nan
        row = {"group": g, "n": int(x.n.iloc[0]), "P(>=5x)": p5}
        for cap in caps:
            vals = [payoff(x.threshold, surv, args.k, cap, a) for a in alphas]
            row[f"V cap {cap:g}x"] = f"{min(vals):.2f}-{max(vals):.2f}"
            row[f"_mid_{cap:g}"] = vals[len(vals) // 2]
        rows.append(row)
    out = pd.DataFrame(rows)
    mid = f"_mid_{caps[len(caps) // 2]:g}"
    out["rank by P(>=5x)"] = out["P(>=5x)"].rank(ascending=False).astype(int)
    out["rank by payoff"] = out[mid].rank(ascending=False).astype(int)
    print(out.drop(columns=[c for c in out if c.startswith("_mid")]).to_string(index=False))


if __name__ == "__main__":
    main()
