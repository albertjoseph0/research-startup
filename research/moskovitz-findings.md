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

## Q1 and Q5. Tail shape by price and which signals matter: open (Nov 1)

Rough extrapolation from the 2015–19 tail slopes (paper value). **This overstates
Series A and B odds (see above).** To be replaced by the Nov 1 queries:

| Joined at | P(≥10×) | P(≥20×) | P(≥33×) | P(≥50×) | P(≥100×) |
|---|---|---|---|---|---|
| Series A | 18% | 12% | 8% | 6% | 4% |
| Series B | 13% | 6% | 4% | 3% | 1% |
| Series C | 8% | 4% | 2% | 1% | 0.6% |
| Series D | 5% | 2% | 0.8% | 0.4% | 0.1% |
| Series E | 3% | 1% | 0.4% | 0.2% | <0.1% |

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
