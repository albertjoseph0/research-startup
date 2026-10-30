"""Fat-tail reading of threshold counts: survival curves, tail slopes with ranges,
extrapolated tail odds, and the chance of at least one hit across several tries.

Usage: python3 tail_analysis.py COUNTS.csv OUT_DIR [--targets 10,20,50,100] [--tries 3]
                                                    [--rho 0,0.3] [--fit-from 2]
                                                    [--stress-alpha 1.1,1.5]

COUNTS.csv columns: group, n, threshold, count
  n         companies in the group
  threshold multiple x (e.g. 2, 5, 10)
  count     companies with outcome >= x

Writes OUT_DIR/tail_summary.csv and, if matplotlib is installed, OUT_DIR/loglog.png.

Method notes (Taleb, Statistical Consequences of Fat Tails): averages are not reported,
because under fat tails they converge too slowly to be useful. Every probability carries
a range. The slope range comes from a parametric bootstrap of the counts, and tail odds
are extrapolated over the whole slope range rather than a single best estimate. The
bootstrap only captures sampling noise; --stress-alpha adds a wider, fixed slope range
for uncertainty about the slope itself (market regime, paper versus cash values).
"""
import argparse
from pathlib import Path

import numpy as np
import pandas as pd


def wilson(k, n, z=1.96):
    """95% Wilson interval for k successes out of n."""
    if n == 0:
        return np.nan, np.nan
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return c - h, c + h


def fit_slope(thresholds, survival):
    """Tail slope alpha from P(>=x) ~ x^-alpha, by least squares on log-log points."""
    ok = survival > 0
    if ok.sum() < 2:
        return np.nan
    slope = np.polyfit(np.log(thresholds[ok]), np.log(survival[ok]), 1)[0]
    return -slope


def bootstrap_slopes(n, thresholds, counts, runs=5000, seed=0):
    """Resample the group's companies across the threshold bins and refit the slope."""
    rng = np.random.default_rng(seed)
    above = np.append(counts, 0)
    bins = np.append(n - counts[0], counts - above[1:])  # below first, then between thresholds
    draws = rng.multinomial(n, bins / n, size=runs)
    surv = np.cumsum(draws[:, ::-1], axis=1)[:, ::-1][:, 1:] / n  # P(>= each threshold)
    return np.array([fit_slope(thresholds, row) for row in surv])


def at_least_once(p, tries, rho=0.0):
    """Chance of at least one hit in `tries` attempts. rho > 0 approximates tries that
    move together by shrinking them to an effective number n / (1 + (n - 1) * rho)."""
    effective = tries / (1 + (tries - 1) * rho)
    return 1 - (1 - p) ** effective


def analyse(counts, targets, tries, rhos, fit_from, stress=None):
    rows = []
    for group, g in counts.groupby("group", sort=False):
        g = g.sort_values("threshold")
        n = int(g["n"].iloc[0])
        x = g["threshold"].to_numpy(float)
        k = g["count"].to_numpy(float)
        tail = x >= fit_from
        alpha = fit_slope(x[tail], k[tail] / n)
        boot = bootstrap_slopes(n, x[tail], k[tail])
        lo_a, hi_a = np.nanpercentile(boot, [2.5, 97.5])
        for xi, ki in zip(x, k):
            lo, hi = wilson(ki, n)
            rows.append({"group": group, "kind": "observed", "multiple": xi, "n": n,
                         "count": int(ki), "p": ki / n, "p_low": lo, "p_high": hi})
        # Extrapolate beyond the last observed threshold over the whole slope range.
        x_last, p_last = x[tail][-1], k[tail][-1] / n
        for t in targets:
            if t <= x_last:
                continue
            ps = [p_last * (t / x_last) ** (-a) for a in (hi_a, alpha, lo_a)]
            row = {"group": group, "kind": "extrapolated", "multiple": t, "n": n,
                   "p": ps[1], "p_low": ps[0], "p_high": ps[2]}
            if stress:
                row["p_stress_low"] = p_last * (t / x_last) ** (-max(stress))
                row["p_stress_high"] = p_last * (t / x_last) ** (-min(stress))
            rows.append(row)
        rows.append({"group": group, "kind": "slope", "alpha": alpha,
                     "alpha_low": lo_a, "alpha_high": hi_a, "n": n})
    out = pd.DataFrame(rows)
    for rho in rhos:
        for col in ("p", "p_low", "p_high"):
            out[f"{col}_{tries}tries_rho{rho:g}"] = at_least_once(out[col], tries, rho)
    return out


def plot(counts, out_path):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib not installed; skipping plot")
        return
    fig, ax = plt.subplots(figsize=(7, 5))
    for group, g in counts.groupby("group", sort=False):
        g = g.sort_values("threshold")
        ax.plot(g["threshold"], g["count"] / g["n"], marker="o", label=group)
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Outcome multiple x (log scale)")
    ax.set_ylabel("Share of companies reaching at least x (log scale)")
    ax.set_title("Survival curves: a straight line means a power-law tail")
    ax.grid(True, which="both", alpha=0.3)
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("counts")
    ap.add_argument("out_dir")
    ap.add_argument("--targets", default="10,20,50,100")
    ap.add_argument("--tries", type=int, default=3)
    ap.add_argument("--rho", default="0,0.3")
    ap.add_argument("--fit-from", type=float, default=2.0,
                    help="lowest multiple used to fit the tail slope")
    ap.add_argument("--stress-alpha", default=None,
                    help="fixed slope range for extrapolation, e.g. 1.1,1.5")
    a = ap.parse_args()
    counts = pd.read_csv(a.counts)
    out = Path(a.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    result = analyse(counts, [float(t) for t in a.targets.split(",")], a.tries,
                     [float(r) for r in a.rho.split(",")], a.fit_from,
                     [float(v) for v in a.stress_alpha.split(",")] if a.stress_alpha else None)
    result.to_csv(out / "tail_summary.csv", index=False)
    plot(counts, out / "loglog.png")
    slopes = result[result["kind"] == "slope"]
    print(slopes[["group", "n", "alpha", "alpha_low", "alpha_high"]].round(2).to_string(index=False))


if __name__ == "__main__":
    main()
