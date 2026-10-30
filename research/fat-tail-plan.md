# Fat-tail revision of the Moskovitz analysis

Startup outcomes are power-law distributed. This changes which numbers matter:
probabilities of crossing large thresholds, and the shape of the tail, rather than
averages or medians.

## 1. What changes in the method

| Earlier approach | Problem with fat tails | Replacement |
|---|---|---|
| Median multiple per group | The median says nothing about the tail, where the money is | Full survival curve: share of companies reaching ≥2×, 5×, 10×, 20×, 50×, 100× |
| "Expected payoff per year" | With tail exponent α ≤ 1 the average is dominated by one or two outliers and is not a usable number; with 1 < α < 2 it is very unstable | Probability of at least one big win in the number of tries you get, and the spread of the best outcome across those tries |
| P(win in 3 tries) = 1 − (1 − p)³ | Assumes the tries are independent; tries in the same market cycle or sector rise and fall together | Estimate how much outcomes move together (by vintage year and sector) and use correlated tries |
| One cohort (2015–19) treated as stable | The tail shape changes with the market regime | Compare tail shape across vintages, including a bad one (2021) |
| Weighted average of percentile ranks | Ranks companies by typical quality, not by their chance of a tail outcome | Weight signals by how much they raise the chance of ≥10× and ≥20×, once tested |
| Small event counts (15–30) read as rates | Tail estimates from few events are unreliable | Report counts with every share, and use tail-slope estimates with ranges |

New considerations that come straight from fat tails:

- **One person, few draws.** An individual gets about three tries per decade, not the
  average across all employees. The useful quantity is the chance of at least one
  large cashed outcome within the decade.
- **Convexity of the employee position.** Salary covers the downside and equity gives
  open-ended upside. Terms that add downside should be avoided: short exercise
  windows, taxes on stock that can't be sold, and large investor preference stacks.
  So should signals that cap the upside, such as early sale talks.
- **Correlation.** 14 of the current top 25 are AI-tagged. Their outcomes will move
  together, so spreading tries across sectors matters.

## 2. What the existing data already shows

Tail slopes from the 2015–19 US cohort (paper value: latest round, IPO or sale value
versus the valuation at the round). α is the slope of the survival curve, P(≥x) ∝ x^−α.
A smaller α means a fatter tail.

| Joined at | ≥3× | ≥5× | ≥10× | α (5×–10×) | α (3×–10×) | P(≥10× on paper) in 1 / 2 / 3 independent tries |
|---|---|---|---|---|---|---|
| Series A | 39.3% | 29.4% | 18.3% | 0.68 | 0.63 | 18% / 33% / 45% |
| Series B | 37.1% | 26.3% | 12.6% | 1.06 | 0.90 | 13% / 24% / 33% |
| Series C | 31.9% | 18.6% | 8.3% | 1.16 | 1.12 | 8% / 16% / 23% |
| Series D | 28.6% | 17.5% | 5.3% | 1.72 | 1.40 | 5% / 10% / 15% |
| Series E | 29.5% | 14.4% | 3.4% | 2.08 | 1.79 | 3% / 7% / 10% |

Read with care: α comes from 2–3 points per stage; paper values include 2021-peak
valuations; companies still private are measured at their latest round.

**Update (published data, see moskovitz-findings.md):** realised venture outcomes have
α ≈ 1.2–1.4 (Correlation Ventures, AngelList), so the paper-based Series A and B slopes
above are too fat. Query 1 now asks for realised (cash) counts at 4 and 8 years
separately, because the tail fattens with holding time. It also asks how many sales
came in below total funding raised, where employee stock can be wiped out.

Cash within 4 years (realised exits only) runs the other way: ≥5× in cash was ~1% for
Series A–C and 5–6% for D–E. So joining earlier gives a fatter tail on paper but a
slower path to cash. The decision is a trade-off between tail fatness and the number
of tries per decade.

## 3. Nov 1 Crunchbase connection plan (200k tokens)

Each query asks for counts at several thresholds, not medians.

**Query 1 – tail by entry price and maturity (~80k).**
> For United States-headquartered companies, take each company's first funding round of each type Series A, B, C, D and E announced between 2015-01-01 and 2019-12-31 that has a disclosed post-money valuation (a company can appear in more than one group). Group by post-money valuation band ($30M to $100M, $100M to $300M, $300M to $1B, $1B to $3B, $3B to $10B) and by stage (early = Series A or B; late = Series C, D or E). Define outcome value as the IPO valuation or acquisition price if disclosed, otherwise the latest disclosed post-money valuation if still private and operating. For each band and stage report: number of companies; number with a known outcome value; counts with outcome value at least 1, 2, 5, 10, 20, 50 and 100 times the round's post-money valuation; counts that went public or were acquired at a disclosed value at least 2, 5, 10, 20 and 50 times the round's post-money valuation, separately within 4 years and within 8 years of the round; count that went public or were acquired at a disclosed value below the company's total funding raised before the sale.

**Query 2 – which observable signals fatten the tail (~80k).**
> Same cohort and outcome definition as before. Group the rounds by (a) the ratio of the round's post-money valuation to the company's previous disclosed post-money valuation (under 1.5x, 1.5x to 3x, over 3x, no prior valuation) and (b) whether a lead investor of the round is one of Sequoia Capital, Andreessen Horowitz, Benchmark, Accel, Founders Fund, Lightspeed Venture Partners, Index Ventures, Greylock, Kleiner Perkins, General Catalyst, Thrive Capital, Khosla Ventures. For each group report: number of companies; counts with outcome value at least 2, 5, 10 and 20 times the round's post-money valuation; counts that went public or were acquired within 6 years at a disclosed value at least 5 and 10 times the round's post-money valuation.

**Query 3 – widen the list (~25k, structured search, not an analytical query).** US Series B and C companies valued $300M–$1.5B with 51+ employees.

**Next cycle (December):** tail shape by vintage year (2015–16 versus 2018–19 versus 2020–21) to measure regime dependence, and the "can you tell by year 2" question.

## 4. Browser agent work (free, now)

- `browser-agent-equity-and-benchmarks.md` (grants, terms, published benchmarks), unchanged.
- `browser-agent-outcome-distributions.md`: published evidence on the shape of startup and venture outcome distributions, and tail exponent estimates.

## 5. How the pieces combine

For each strategy (entry price band × years per try), compute the probability of at
least one cashed ≥10× (and ≥20×) outcome within 10 years. Do it for independent tries
and for correlated tries. Combine with grant size (your share) to turn multiples into
dollars, and compare with the founder path's tail from published data.

## 6. Changes made (2026-10-30)

**Pool instead of ranking.** `score_all.py` now groups companies into tiers instead of
relying on rank order:

| Tier | Rule |
|---|---|
| A – core pool | No fragility flag, and in the top 25 in at least 80% of 2,000 runs where every weight is scaled by a random 0.5–1.5 |
| B – wider pool | No fragility flag, and in the top 50 in at least 50% of runs |
| C – rest | Everything else without a fragility flag |
| F – fragile | Any fragility flag (below) |

Within a tier, companies are treated as roughly equal bets. Choose between them on your
own terms and fit (grant size, exercise window, tender history, software roles, sector
spread), not on small score differences.

**Fragility screens** (remove exposures that cap the upside or add downside):

- money raised is half or more of the latest valuation, so a mid-sized sale can wipe out employee stock
- a down round
- a layoff mention in the last 2 years
- no new round in 2 years
- reported sale talks

**Sector column** (AI / non-AI), to spread tries across sectors, since tries in the same
sector and cycle move together.

**`tail_analysis.py`** reads threshold counts (such as the Nov 1 query results) and writes:
- survival curves on log-log axes (a straight line means a power-law tail)
- the tail slope with a bootstrap range
- extrapolated odds at 10×, 20×, 50× and 100×, over the bootstrap range and over a fixed stress range (`--stress-alpha 1.1,1.5`) for uncertainty about the slope itself
- the chance of at least one hit in N tries, both independent and moving together (`--rho`)

No averages are reported.

## 7. Personal rules to decide before applying (proposal)

These follow from fat tails, ruin avoidance and the barbell idea in Taleb's *Skin in
the Game* and *Antifragile*:

1. **Fixed option budget.** Decide in advance the most cash you will ever spend buying
   options, plus the tax on them. Never borrow for it.
2. **Keep only winners.** When leaving a company, buy vested options only if it shows
   winning signals: a new round at a higher valuation, a tender above the previous
   price, or fast revenue growth. Otherwise let them go.
3. **Prefer long exercise windows and tender offers.** They let you keep the tail
   without spending the budget early. Ask about both at every offer.
4. **Sell part, keep part.** When a tender comes, sell some (median tenders allow about
   20%) to lock in cash and keep the rest for the tail.
5. **Spread tries across sectors** rather than three AI companies in a row.
6. **No ruin moves.** No salary you can't live on, no tax bill on stock you can't sell,
   no borrowing against illiquid shares.
