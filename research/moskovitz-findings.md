# Moskovitz's argument tested with 2026 data: findings so far

Sources: Crunchbase cohort queries (US companies that raised in 2015–19), the browser
agent's research (Levels.fyi, company sites, Carta, Cooley, Jay Ritter's IPO data,
EquityBee, Index Ventures, Holloway, Scalar), and the scored company list.
All figures were checked against their sources on 2026-10-30.

## Q2. Is employee stock likely to be worth more than $0? Largely answered

- Investor terms are mostly employee-friendly. 94–98% of venture deals have a 1×
  liquidation preference, and 95–96% have non-participating preferred (Cooley,
  Q1 2025 to Q1 2026).
- So employee common stock is wiped out only if a sale comes in below roughly the
  total money raised. Across the scored list, money raised is a median of 24% of the
  current valuation (9% to 49% in the top 25).
- Employee common stock is usually valued at 30–45% of the investor share price
  (Scalar). Rule of thumb: about 20% at Series A, about 30% at Series B. This sets the
  option strike price, so it sets what it costs to buy your options.

## Q3. What share of the company does an employee get? Roughly answered

| Source | Stage | Grant |
|---|---|---|
| Index Ventures (2018 seed data) | Seed | 0.45% mid-level engineer, 1.0% senior |
| Holloway (2022) | Just after Series A | 0.33–0.66% senior engineer |
| Index Ventures worked example | Series A at $40M | 0.1% senior developer ($40K grant) |
| EquityBee (9,000+ grants, 2026) | Seed/A, B, C, D+ | Median new-hire grant value $20K, $29K, $41K, $62K (all roles; engineering ICs $23.2K) |

Turning EquityBee's grant values into shares (common at 30–45% of the investor price,
at today's median valuation for each round):

| Round | Median valuation 2026 | Share of company |
|---|---|---|
| Series B | $353M | 1.8–2.7 bp (0.018–0.027%) |
| Series C | $878M | 1.0–1.6 bp |
| Series D+ | $1.15B | 1.2–1.8 bp |

Levels.fyi four-year grants, priced at the investor share price:

| Company | Grant (4 years) | Share | Value at 10× |
|---|---|---|---|
| Eve ($1B) | $200K | 2.0 bp | $2.0M |
| Deepgram ($1.3B) | $140K | 1.1 bp | $1.4M |
| Cape ($0.9B) | $115K | 1.3 bp | $1.1M |
| Snorkel AI, senior ($3.5B) | $382K | 1.1 bp | $3.8M |
| Snorkel AI, entry ($3.5B) | $140K | 0.4 bp | $1.4M |
| Muon Space ($1.5B) | $58K | 0.4 bp | $0.6M |
| Kong ($2B) | $42K | 0.2 bp | $0.4M |

Findings:
- Grant dollars rise about 3× from Seed/Series A to Series D+, while valuations rise
  far more, so your share falls steeply with stage.
- Moskovitz's 5 bp at $500M (2017) or 10 bp at Facebook employee #100 (2013) now
  corresponds roughly to a Series A or early Series B company. At a $1B Series C or D
  company, a typical engineer gets about 1–2 bp.
- In dollars, the grant at a ~$1B company is about $100–400K over four years, so a
  10× outcome is worth about $1–4M. Moskovitz's $10M example needs 25–100× from
  today's entry prices, which sits deep in the tail.
- Levels.fyi data is thin: individual entries are hidden when logged out, and only
  about 12 of the 62 companies show a median package. A $0 stock figure on Levels
  often means options weren't valued, not that no equity was granted.

## Q4. How soon can you get cash? Largely answered

Jay Ritter's IPO data (median company age at IPO, and venture-backed IPOs per year):

| Years | Median age at IPO | Venture-backed IPOs per year |
|---|---|---|
| 1980–89 | 7.5 | 51 |
| 1990–98 | 9.1 | 141 |
| 1999–2000 | 5.5 | 262 |
| 2001–09 | 12.2 | 40 |
| 2010–19 | 10.9 | 71 |
| 2020–21 | 10.0 | 144 |
| 2022–25 | 11.0 | 31 (14, 23, 37, 49) |

- Companies go public later than in the 1980s and 1990s, and since 2022 there have
  been far fewer venture-backed IPOs.
- Tender offers partly fill the gap. On Carta in H1 2025, 61% of tenders were at
  Series C or later. Median participation was 46% at seed to Series B and 66% at
  Series C+, up from 37% in 2021.
- Equity terms: every company with stated terms grants stock options (10 of the top
  25). No RSU grants were found. Vesting is the standard four years with a one-year
  cliff. Only Hightouch has a documented extended exercise window (10 years).
- Consequence for trying several companies: leaving after two years usually means
  buying vested options within about 90 days, at a strike price of 30–45% of the
  investor price, plus tax on the gap. That adds downside to each try.

## Q6. What are founder odds today? Answered

- Carta's 2018 seed class: 62% shut down within 7 years; 1.3% became unicorns.
  Moskovitz's 2017 figure was about 1%.
- Only 15–17% of seed-funded companies from the 2022–23 cohorts reached Series A
  within two years. CB Insights found 48% of 2008–10 seed companies raised a second
  round (no time limit stated).
- Founding-team ownership (Carta, rounds raised 2021–25): 56% after seed, 36% after
  Series A, 22–27% at Series B, 16% at Series C. That is the whole team; split across
  2–3 founders, each holds roughly 5–8% by Series C.

## Tail shape from published, realised outcomes

Venture outcomes measured at exit (cash), not at the latest private valuation:

| Source | Sample | <1× | 1–2× | 2–5× | 5–10× | 10–50× | 50×+ |
|---|---|---|---|---|---|---|---|
| Correlation Ventures | 27,259 US financings, 2009–18 | 65% | 18% | 8% | 5% | 3.6% | 0.4% |

- Horsley Bridge (about 7,000 investments, 1985–2014): about half lost money; 6% returned
  10× or more and produced 60% of all returns.
- Correlation Ventures (2004–13, 21,000+ financings): 10% returned 5×+, 4% returned 10×+.
- Tail slope α (survival convention, P(≥x) ∝ x^−α): 1.17 between 5× and 10×, 1.43 between
  10× and 50× (Correlation 2009–18); 1.32 between 5× and 10× (2004–13). AngelList (1,808
  early investments, Clauset method) reports α = 2.3 in the density convention, which is
  about 1.3 in the survival convention. So realised venture outcomes have α ≈ 1.2–1.4:
  the average exists, but the spread is enormous.
- **The tail grows fatter the longer investments are held.** AngelList data summarised by
  McDonald (secondary source): α ≈ 4.0 after 1 year, 2.0 after 2, 1.3 after 3, 1.1 after 4,
  1.0 after 5, 0.8 after 8 years.

**Correction to the earlier estimate:** our 2015–19 cohort data gave α ≈ 0.65 (Series A)
and ≈ 1.0 (Series B). Those used paper values (latest private rounds, including 2021-peak
prices), which make the tail look fatter than realised outcomes. The extrapolated
table below therefore overstates Series A and B odds.

**Regime dependence is strong.** Venture fund median TVPI is 2.15× for 2014–17 vintages
and 1.30× for 2018–21 (Dakota). Against the S&P 500 (KS PME) it is 1.12 for 2014–17 and
0.84 for 2018–21 (Cambridge Associates via Lambda). Cash actually returned (DPI) by
2017 and 2018 funds is only 0.31× and 0.15× of capital after 8–9 years. Recent vintages
are weaker and slower to pay out than the 2015–19 companies we measured.

### What this means for one employee try

Anchored on realised data (4% of financings reach 10×, 0.4% reach 50×, α ≈ 1.3–1.45),
for a $150K grant (four years, valued at the investor price):

| Outcome | Multiple | Value | Chance per try | At least once in 3 independent tries |
|---|---|---|---|---|
| Good | 10× | $1.5M | ~4% | ~11.5% |
| Very good | 20× | $3M | ~1.5% | ~4.4% |
| Moskovitz's example | 50–100× | $7.5–15M | ~0.15–0.4% | ~0.5–1.2% |

These are venture-wide, mostly early-stage odds. Later-stage entry is likely lower (in
our 2015–19 data, a 5× cashed exit within 4 years happened for ~1% of Series C
companies). Correlated tries lower the three-try figures further.

### Founder outcomes (for comparison)

- 84–88% of venture-backed founders receive nothing at exit; the top 2% capture about
  80–89% of all founder exit value (NBER working paper 34512; Dealroom summary,
  1987–2025).
- The average founder payoff is $5.6M, but the top percentile is $661M. The average is
  produced by the tail; the typical founder gets $0.
- Common stock can get nothing at mid-sized exits because investors are paid first:
  FanDuel sold for $465M against $559M of investor preferences, and common received $0.
  This happens mainly in $50–500M exits.

### Employee option behaviour

- 85% of option grants have a 90-day window to buy after leaving (Carta, 2022).
- 46% of in-the-money options expiring in 2022 went unexercised. Only 28% were exercised
  during the post-leaving window. 23% of employees who didn't exercise said they
  couldn't afford it.
- Tender offers: the median allows selling 20% of eligible shares, at no discount
  (median), and is fully subscribed at Series C+. Median tender size is $27.6M at
  Series C+ and $5M at Series B and earlier.

## Q1 and Q5. Tail shape by price and which signals matter: answered (Nov 1)

Cohort: US companies, each company's first Series C, D or E round (or A or B where noted)
announced 2015–19 with a disclosed post-money valuation. Outcome: an IPO or acquisition at
a disclosed value, measured against that round's valuation, up to Nov 2026. These are cash
exits only. Companies still private count as no exit, and so do sales at an undisclosed
price. Ranges are 95% intervals.

**Q1. Entry price.** A cheaper entry did not leave more room to grow. Higher-priced rounds
were more likely to end in a large cash exit.

| Entry round | Companies | IPO | Acquired | Closed | ≥2× cash | ≥5× cash | ≥10× cash | ≥20× cash |
|---|---|---|---|---|---|---|---|---|
| A–B, $30M–100M | 3,548 | 25 | 934 | 409 | 5.5% | 3.6% (3.0–4.3) | 1.9% (1.5–2.4) | 1.0% (0.8–1.4) |
| C–E, $100M–300M | 788 | 11 | 311 | 114 | 8.1% | 3.0% (2.1–4.5) | 1.8% (1.1–3.0) | ~0.9% (extrap.) |
| C–E, $300M–1B | 541 | 71 | 202 | 67 | 17.4% | 9.1% (6.9–11.8) | 3.7% (2.4–5.6) | ~1.9% (extrap.) |
| C–E, $1B–3B | 185 | 86 | 56 | 16 | 43.8% | 21.6% (16.3–28.1) | 5.9% (3.4–10.3) | ~2.6% (extrap.) |
| C–E, over $3B | 33 | 19 | 6 | 2 | 42.4% | 12.1% (4.8–27.3) | 3.0% (0.5–15.3) | ~1.0% (extrap.) |

- Tail slope (α, survival curve from 2× up) is about 0.95 at $100M–1B, 1.2 at $1B–3B and
  0.73 for early rounds. Realised venture tails elsewhere run 1.2–1.4.
- **Price was a quality signal.** In 2015–19 a $1B+ Series C–E round was the top ~12% of
  its stage. Today the median Series C is $878M, so the same absolute price no longer
  marks the same selectivity. Read the lesson as "the premium-priced companies of their
  stage and year did best," not "$1B–3B is the band."
- **Bias that flatters the expensive bands.** Valuations are disclosed more often for
  companies that later IPO (often in their S-1). In the $300M–1B group, 72 companies had
  no earlier disclosed valuation, and 66 of them exited. Small acquisitions at
  undisclosed prices are also counted as no exit.
- **Early rounds:** the slope is fatter, but the level is low and cash is slow. Within
  this window, 1.0% reached a ≥20× cash exit.

**Q5. Signals,** tested on the $300M–1B Series C–E group.

| Signal | Companies | ≥2× cash | ≥5× cash | ≥10× cash |
|---|---|---|---|---|
| Lead investor one of 12 top firms¹ | 53 | 30.2% | 24.5% (14.9–37.6) | 11.3% (5.3–22.6) |
| Other lead | 488 | 16.0% | 7.4% (5.4–10.0) | 2.9% (1.7–4.8) |
| Step-up under 1.5× the previous valuation | 88 | 13.6% | 4.5% | 2.3% |
| Step-up 1.5–3× | 250 | 6.4% | 3.6% | 1.2% |
| Step-up over 3× | 131 | 8.4% | 5.3% | 0.8% |

¹ Sequoia, a16z, Benchmark, Accel, Founders Fund, Lightspeed, Index, Greylock, Kleiner
Perkins, General Catalyst, Thrive, Khosla.

- A top-tier lead roughly tripled the rate of ≥5× and ≥10× cash exits. It rests on 13 and
  6 events, so the true lift could be anywhere from about 2× to 5×.
- The size of the step-up showed no link to cash outcomes.

**Holding time and market timing** ($300M–1B Series C–E group, by year of the round):

| Round year | Companies | ≥5× cash ever | ≥5× cash within 4 years | ≥10× ever | ≥10× within 4 years |
|---|---|---|---|---|---|
| 2015–16 | 148 | 12.2% | 1.4% | 5.4% | 0% |
| 2017 | 88 | 14.8% | 9.1% | 4.5% | 1.1% |
| 2018–19 | 305 | 5.6% | 4.6% | 2.6% | 2.0% |

- **Big wins take time.** For 2015–16 rounds, 16 of the 18 ≥5× exits came after year 4.
- **The exit window matters.** The 2017 and 2018–19 groups reached the 2020–21 IPO window
  inside 4 years; 2015–16 did not. That swung the 4-year odds about 6×, and tries made in
  the same years rise and fall together.
- The 2018–19 "ever" figures are lower partly because those companies have had less time.

**Per try, joining a $300M–1B company:**
- ≥5× cash: about 9% (7–12%).
- ≥10× cash: about 4% (2–6%).
- With a top-tier lead: about 25% and 11%.

**Over 3 tries that move together somewhat (correlation 0.3):**
- At least one ≥10×: about 7% (4–10%).
- With top-tier leads every time: about 20% (10–38%).

**Not answerable with this data:**
- **Headcount at the time of joining.** Crunchbase shows only today's headcount, which
  reflects the outcome. So the 101-employee cut-off can't be tested historically. Keep a
  floor of about 11 employees as a scale check only.
- **"Can you tell by year 2"** was not run, to stay within the token budget.

## Can you tell by year 2? Yes (Nov 2 queries)

**The question.** Same cohort as Q1. Group companies by what happened in the 24 months
after their round, then count cash exits at any time up to now. Ranges are 95% intervals.

**$300M–1B group:**

| In the 24 months after the round | Companies | ≥2× cash | ≥5× cash | ≥10× cash |
|---|---|---|---|---|
| Raised again at a higher disclosed valuation | 211 | 21.8% | 15.6% (11.4–21.2) | 6.6% (4.0–10.8) |
| Raised again, valuation not disclosed | 84 | 19.0% | 13.1% (7.5–21.9) | 4.8% |
| Raised again at the same or a lower valuation | 7 | 0 | 0 | 0 |
| No new round and no exit | 199 | 5.5% | 1.5% (0.5–4.3) | 0.5% |
| Sold or went public within 24 months | 40 | 32.5% | 2.5% | 2.5% |

**$1B–3B group:**

| In the 24 months after the round | Companies | ≥5× cash | ≥10× cash |
|---|---|---|---|
| Raised again | 126 | 27.8% (20.7–36.2) | 7.9% |
| No new round and no exit | 33 | 3.0% | 0 |
| Sold or went public within 24 months | 26 | 11.5% | 3.8% |

**What it shows.**

- **Raising again is the signal.** Across both groups, a company that raised again within
  2 years reached a ≥5× cash exit 18.8% of the time (79 of 421). One that neither raised nor
  exited managed it 1.7% of the time (4 of 232). That is about a tenfold gap. At ≥10× it is
  6.7% against 0.4%.
- **The valuation isn't needed.** Rounds with an undisclosed valuation did about as well as
  disclosed up-rounds (13.1% against 15.6%).
- **Early exits are mostly small.** Sales or IPOs within 2 years often returned 2×, but
  rarely 5×.
- **Caveat.** "Raised again" partly means "still alive and wanted by investors", which is
  exactly the information an employee has at year 2. Disclosure bias (see Q1) applies here
  too.

**What it means for one employee.** Checking at year 2 is a nearly free filter.
- If the company has not raised a new round (or been sold) by then, its chance of a 5× cash
  exit falls to about 1–2%. Leave, and don't spend cash buying its options.
- If it has raised again, the chance rises to roughly 15–28%. That's the case for staying, or
  for buying your vested options if you leave.

This supports the "keep only winners" rule and the "no new round in 2 years" fragility
screen.

## Re-test on 2010–14 rounds (Nov 6)

**The question.** Do the 2015–19 findings hold in an earlier, independent set of companies
that has had more time to exit? This set is US companies whose first Series C, D or E round
came in 2010–14, with a disclosed valuation, counting cash exits up to Nov 2026. Fewer
valuations were published then, so the groups are smaller.

**Entry price:**

| Valued at the round | Companies | ≥2× cash | ≥5× cash | ≥10× cash |
|---|---|---|---|---|
| $100M–300M | 283 | 12.0% | 6.7% (4.3–10.2) | 2.8% |
| $300M–1B | 67 | 29.9% | 6.0% (2.3–14.4) | 4.5% |
| $1B–3B | 22 | 50.0% | 27.3% (13.2–48.2) | 18.2% |
| over $3B | 6 | 33% | 0 | 0 |

**Lead investor** ($100M–3B rounds):

| Lead investor | Companies | ≥2× cash | ≥5× cash | ≥10× cash |
|---|---|---|---|---|
| One of the 12 top-tier firms | 42 | 35.7% | 26.2% (15.3–41.1) | 19.0% |
| Other | 331 | 15.1% | 5.4% (3.5–8.4) | 2.1% |

**Year 2** ($100M–3B rounds):

| In the 24 months after the round | Companies | ≥5× cash | ≥10× cash |
|---|---|---|---|
| Raised again | 247 | 9.3% (6.3–13.6) | 5.7% |
| No new round, no exit | 116 | 2.6% (0.9–7.3) | 0 |
| Sold or went public | 10 | 20% | 0 |

**What replicated.**
- **Top-tier lead: yes, strongly.** About five times the ≥5× rate and nine times the ≥10×
  rate. Across both sets it is 25.3% (24 of 95) against 6.6% (54 of 819) at ≥5×, and 14.7%
  against 2.6% at ≥10×. This is now the best-supported signal in the analysis.
- **Year 2: yes, more weakly.** 9.3% against 2.6% at ≥5× (15.3% against 2.0% across both
  sets).
- **Price: only at the top.** $1B–3B rounds again did best (27%). But $100M–300M and
  $300M–1B were the same (about 6%), so the steady rise with price seen in 2015–19 didn't
  repeat. The companies priced at the top of their era stood out; below that, price told
  little. The payoff check (`tail_payoff.py`) agrees: it ranks $1B–3B and top-tier-lead
  rounds far above the rest, and swaps the two lower bands.

**Scoring changes** (`score_all.py`):
- the investor weight rises from 0.15 to 0.20;
- the price weight falls from 0.10 to 0.05.

## Checks from Taleb, *Statistical Consequences of Fat Tails* (arXiv 2001.10488, 3rd ed. 2025)

Five results from the book apply directly. Each was checked against our numbers.

**1. Compare payoffs, not probabilities (ch. 11).** Taleb shows that ranking by the chance of
crossing a threshold (a "binary" view) can disagree with ranking by payoff (a "vanilla" view)
when tails differ, and that "one should never operate in probability space". An employee's
grant pays like an option, so `tail_payoff.py` recomputes every group's expected cash payoff
above 2×, per $1 of grant value.
- Between observed thresholds it interpolates the survival curve on log-log axes.
- Above 10× it uses tail exponents of 1.1–1.5.
- It caps outcomes at 100×, 300× or 1,000× the entry price.

| Group | P(≥5× cash) | Expected payoff above 2×, per $1 of grant (cap 300×) | Rank by probability | Rank by payoff |
|---|---|---|---|---|
| C–E $300M–1B, top-tier lead | 24.5% | 3.5–4.9 | 1 | 1 |
| C–E $1B–3B | 21.6% | 2.4–3.2 | 2 | 2 |
| C–E over $3B | 12.1% | 1.5–1.8 | 3 | 3 |
| C–E $300M–1B | 9.1% | 1.3–1.7 | 4 | 4 |
| C–E $300M–1B, other lead | 7.4% | 1.0–1.4 | 5 | 5 |
| A–B $30M–100M | 3.6% | 0.7–0.9 | 6 | 6 |
| C–E $100M–300M | 3.0% | 0.6–0.8 | 7 | 7 |
| Year 2: raised again | 18.8% | 2.3–3.1 | – | – |
| Year 2: no round, no exit | 1.7% | 0.2–0.3 | – | – |

**Result:** the order is identical under both views, so the price, lead-investor and year-2
conclusions survive this check. The figures count only cash exits above 2×; still-private
companies count as zero.

**2. Expected values are mostly hidden (ch. 9, ch. 17).** For tail exponents of 1.1–1.5 and
samples of 100–10,000, a large share of the true mean lies above the largest value observed
(Taleb, figs. 9.7–9.8). The payoffs above confirm this. Raising the cap from 100× to 1,000×
adds about 15–50% to every group's payoff, and that range is set by outcomes almost never seen in
the data. So expected value can't justify a decision here. Taleb's "shadow mean" handles this
by bounding the support, which is what the cap does. Use the chance of at least one large
cash outcome, and avoid ruin, rather than an average.

**3. Three tries are nowhere near enough to average (ch. 8).** Taleb's κ measures how fast
averages settle. A Pareto tail with α = 1.25 has κ ≈ 0.83, and matching the stability that a
Gaussian reaches with 30 observations takes about 4×10⁸ observations (eq. 8.8; at α = 1.5,
about 2×10⁵). A career of 3 tries is a draw from the tail, not an average of it. That's why
this analysis reports "at least one ≥10× in N tries" and never an expected payoff per year.

**4. Uncertainty about α fattens the tail (ch. 20–21).** When the tail exponent itself is
uncertain, the true tail is fatter than the one at the average α, by Jensen's inequality. So
for the extrapolated 20× and 50× odds, the low-α end of the stress range is the more realistic
one. The ≥5× and ≥10× figures are observed counts and aren't affected.

**5. Lindy and the absorbing barrier (ch. 23).** Taleb models survival as distance from an
absorbing barrier. A process with zero drift has power-law ("Lindy") survival, but any amount
of negative drift turns it into a fast exit. For a startup, the barrier is running out of cash
and the drift is burn net of new money. This explains the year-2 result: a company that
hasn't raised in 2 years is drifting toward the barrier, and its odds of a 5× exit fall to
about 1–2%. In practice, the questions that measure distance and drift are how many months of
cash the company has and how much it burns. Both are already on the interview list.

## What this does to Moskovitz's comparison

- **His risk claim holds.** Employee stock is very likely worth more than $0 if the
  company survives: standard investor terms, and most top companies have raised far
  less than their valuation.
- **His dollar claim weakens at today's prices.** For an engineer at a ~$1B company, a
  realistic good outcome is $1–4M, not $10M. Matching his $10M needs a senior-level
  grant plus an outlier, or joining around Series A/B, where the share of the company
  is 5–10× larger and the tail is fatter but cash is slower.
- **His speed claim weakens.** Fewer IPOs and later IPOs mean tender offers matter
  more, and options with 90-day exercise windows make leaving after two years costly.
- **The founder path is about as hard as he said:** 1.3% unicorn rate, 62% shut down,
  and 84–88% of founders get nothing at exit. A founder's share at success is still
  roughly 5–8% each, far larger than an employee's 1–10 bp.
- **Fat tails change how to do several tries.** Big outcomes come from holding winners
  for years (the tail fattens with holding time), not from cashing out every two years.
  The strategy that fits the data is to leave losers quickly and keep the shares of
  winners. Keeping them means buying vested options when you leave, so you need either
  cash set aside for that or a company with a long exercise window. Only Hightouch has
  a documented one in the top 25.
