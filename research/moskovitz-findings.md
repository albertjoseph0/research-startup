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

## Q1 and Q5. Tail shape by price and which signals matter: open (Nov 1)

Rough extrapolation from the 2015–19 tail slopes (paper value), to be replaced by the
Nov 1 queries:

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
- **The founder path is about as hard as he said:** 1.3% unicorn rate, 62% shut down.
  A founder's share at success is still roughly 5–8% each, far larger than an
  employee's 1–10 bp.
