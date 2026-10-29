# Which funding stage should an employee join? — Crunchbase cohort study

Goal: test the stage filter in Dustin Moskovitz's "join a high-growth, relatively low-risk
company" argument (written ~2013, when "Series B–E" was the implied sweet spot) against
outcome data, instead of assuming it.

Objective per entry stage (employee view): growth multiple from entry valuation,
probability of a bad outcome, and time to a liquid outcome (more tries per career).

All data: Crunchbase MCP, queried 2026-10-29. US-headquartered companies.

## Query 1 — liquidity / status (cohort: first Series A/B/C announced 2016-01-01 → 2018-12-31)

Request ID `a3097ba7e8aa10a4fe142d7302c532b9`

| Entry | Companies | Acquired | IPO | Still private |
|---|---|---|---|---|
| Series A | 4,474 | 29.9% | 5.2% | 57.5% |
| Series B | 2,172 | 37.3% | 10.5% | 50.7% |
| Series C | 1,008 | 43.4% | 17.6% | 40.4% |

"Closed" (~26% at every stage) overlaps with acquisitions (absorbed companies) and is excluded.

## Query 2 — realised exits only (same window)

Request ID `4915c78337ffae6eece47a77579a1ece`. Cohort assignment differed from query 1
(each company appears to have been counted once), so B/C counts are smaller.

| Entry | Companies | Median entry post-money | Disclosed exits | Median exit | Exit ≥5× entry | Exit ≥$1B |
|---|---|---|---|---|---|---|
| Series A | 4,469 | $28.6M | 436 | $428M | 100 (2.2%) | 117 (2.6%) |
| Series B | 1,387 | $66.0M | 244 | $426M | 30 (2.2%) | 63 (4.5%) |
| Series C | 605 | $143.3M | 155 | $515M | 15 (2.5%) | 59 (9.8%) |

## Query 3 — multiples marked to market (cohort: first round of each type A–E, 2015-01-01 → 2019-12-31, disclosed post-money required; a company can appear in several groups)

Request ID `10c320eaa0e59142bc16a972f21a9e7d`. Cost ≈ 86k data tokens.

Outcome value = IPO valuation or acquisition price if disclosed; otherwise, if still
private and operating, the latest disclosed post-money valuation. No outcome value
(closed, or exited at an undisclosed price) is counted as a bad outcome below, which is
conservative: some undisclosed exits are modest wins.

| Entry | Companies | Median entry post-money | Median multiple (known) | ≥3× | ≥5× | ≥10× | <1× | No value | Bad (<1× or no value) | P(≥5× in 3 tries) |
|---|---|---|---|---|---|---|---|---|---|---|
| Series A | 5,636 | $29M | 2.85× | 39.3% | 29.4% | 18.3% | 2.2% | 19.8% | 22.0% | 65% |
| Series B | 2,617 | $79M | 2.78× | 37.1% | 26.3% | 12.6% | 4.1% | 22.2% | 26.3% | 60% |
| Series C | 1,234 | $165M | 2.41× | 31.9% | 18.6% | 8.3% | 5.8% | 24.0% | 29.7% | 46% |
| Series D | 567 | $327M | 1.98× | 28.6% | 17.5% | 5.3% | 8.5% | 21.0% | 29.5% | 44% |
| Series E | 264 | $584M | 2.10× | 29.5% | 14.4% | 3.4% | 9.1% | 19.3% | 28.4% | 37% |

## Reading the three together

1. **On paper, earlier wins.** Marked to market, the chance of a ≥5× or ≥10× multiple falls
   steadily from A to E, while the bad-outcome rate does not fall with stage (~22–30%).
   Later stages buy no measurable safety in this data — the core premise of "B–E is lower
   risk" does not show up.
2. **In cash, later wins.** Realised ≥5× exits are ~2% at every stage (query 2), and the
   gap between 2% realised and 29% marked is mostly unrealised paper value. Over half of
   the Series A cohort is still private 8–10 years later (query 1). Paper marks from the
   2021 peak inflate the earliest cohorts most.
3. **So stage is a trade between multiple and time-to-liquidity, not between multiple and
   risk.** The decision variable that matters for "2–3 tries per career" is a
   time-adjusted multiple, which these queries do not yet measure.

## Query 4 — time to liquidity (same cohort as query 3)

Request ID `35908fbe96ffb536146589be7b6fb3e5`. Cost ≈ 82k data tokens.

"Cash 5×" = IPO or acquisition within 4 years of the entry round, at a disclosed value
≥5× the entry post-money. 95% Wilson intervals in brackets.

| Entry | Exited (any time) | Median years to exit | Liquid ≤4y | Liquid ≤6y | Cash 5× ≤4y | P(cash 5× in 3 tries) | Paper ≥5× (query 3) |
|---|---|---|---|---|---|---|---|
| Series A | 23.6% | 4.9 | 9.0% | 15.3% | 0.87% (0.7–1.1) | 2.6% | 29.4% |
| Series B | 30.9% | 4.4 | 13.7% | 20.9% | 1.26% (0.9–1.8) | 3.7% | 26.3% |
| Series C | 39.7% | 4.4 | 17.5% | 27.5% | 0.89% (0.5–1.6) | 2.7% | 18.6% |
| Series D | 44.8% | 3.7 | 24.2% | 32.8% | 4.76% (3.3–6.8) | 13.6% | 17.5% |
| Series E | 58.0% | 3.5 | 32.6% | 46.6% | 6.06% (3.8–9.6) | 17.1% | 14.4% |

Findings:

1. Liquidity rises monotonically with stage: 9% of Series A entrants are liquid within
   4 years versus 33% at Series E.
2. On the time-adjusted measure Moskovitz's argument actually needs (a big, cashed-out
   outcome within one "try"), Series D/E beat A–C by ~4–5×, and the intervals do not overlap.
   A–C are statistically indistinguishable from each other at ~1%.
3. Paper and cash rankings invert: A is best on paper (29% ≥5×) and worst in cash (<1%
   within 4 years).
4. Even the best stage gives ~17% odds of a cashed 5× across three 4-year tries, far
   below "within 2 or 3 tries, and likely on the first one" for an unselected company.
   The argument depends on picking well within the stage, not on the stage itself.

Confounds specific to this query:

- **Bubble timing.** D/E rounds from 2015–2019 plus ~4 years lands exits in the 2020–2021
  IPO/SPAC window at peak valuations; A–C entrants mostly missed that window. The D/E
  advantage may be partly a vintage effect. Query 3 of the drift study below tests this.
- **Disclosure bias.** IPOs always disclose a valuation; acquisitions often do not. Later
  stages exit more by IPO, so a disclosed ≥5× exit is easier to observe for D/E.
- Small counts for D/E (27 and 16 events).

## Caveats

- Requires a disclosed post-money valuation at entry; disclosure skews toward prominent companies.
- Marks are preferred-share prices; employee common/options are worth less, and options
  have a strike price, which changes the payoff shape.
- Crunchbase under-reports closures; "still private" includes zombies.
- 2015–2019 cohorts predate the AI-era round inflation; drift is untested.

## Next queries (each ≈ 80–90k data tokens)

1. ~~Time-adjusted~~ — done, query 4.
2. Zombie correction: share of "still private" with no funding round since 2023-01-01.
3. Drift: query 3 split into 2015–2016 vs 2018–2019 cohorts.
4. Sector: query 3 split AI vs non-AI.
