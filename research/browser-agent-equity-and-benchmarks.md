# Browser agent: equity grants, equity terms and published benchmarks

This round collects the numbers needed to test Dustin Moskovitz's argument for joining a
fast-growing private company instead of founding one. Part 1 is about what an employee
actually gets: grant size, stock type, how long you have to buy options, and tender
history. Part 2 collects published research on founder odds, time to IPO, and how
employee stock is treated.

Parts 1 and 2 are independent. Run them in parallel if you can.

---

## Rules

1. **Read only.** Do not log in, sign up, enter an email address, fill in any form,
   download anything that is behind a form, or contact anyone. If a page or report is
   gated, record `gated` and move on.
2. **Do not use LinkedIn, Glassdoor or Blind.** For web searches use DuckDuckGo or Bing;
   Google blocks automated searches.
3. **Never estimate.** Copy numbers exactly. Every value needs a source URL and the
   sentence or table row it came from (`quote`). If a number is read off a chart with no
   data labels, record it but set `confidence` to `low` and note `read from chart`.
4. **Work in batches of 8 companies** in Part 1. After each batch, paste that batch's
   CSV rows into your reply so nothing is lost if the browser crashes.
5. **Follow each company's real website,** found from its Crunchbase profile or a search
   for its name. Several names are shared with other companies (Rain, Cape, Port, Omni,
   Eon, Solace, Owner, Kong). Check the company's description matches before recording.

---

## Part 1 – What an employee gets

### 1A. Levels.fyi stock grants (all 62 companies below)

For each company, open its Levels.fyi page (logged out) and look at **US software
engineer** data. Record, as separate rows, **up to 10 of the most recent individual
offers or salary entries** that show a stock figure. For each entry:

`company, crunchbase_url, levels_url, entry_date, level, years_of_experience, location, base_usd, stock_per_year_usd, bonus_usd, total_usd, stock_type_if_shown, vesting_if_shown, confidence, notes`

Also record one summary row per company with `entry_date = summary` and the company
page's own median total pay, median stock per year, stock type (RSU or options) and
vesting schedule, if shown.

If the company has no Levels.fyi page, or no US software engineer data, write one row
with `notes = None found`. Some companies use a longer page name, e.g.
`reliable-robotics-corporation`; search Levels.fyi for the company before concluding
it has no page.

Output: **`levels_grants.csv`**

### 1B. Equity terms (the first 25 companies only)

For each, look on its careers page, job postings, benefits page, engineering blog or
public handbook. Also check the public list of companies with extended exercise windows
on GitHub (`github.com/holman/extended-exercise-windows`) and recent news. Record:

| Column | Question |
|---|---|
| `stock_type` | Does the company grant stock options, RSUs, or both to new employees? |
| `exercise_window` | How long after leaving can employees buy their vested options? (e.g. `90 days`, `7 years`, `10 years`) |
| `vesting_schedule` | e.g. `4 years, 1-year cliff` |
| `tender_history` | Any employee tender offer or company-run share sale, with dates and valuation. This is a deeper check: search news, the company blog and investor announcements with the words "tender", "secondary" and "liquidity". `None found` if nothing |
| `equity_refresh` | Any statement about refresh grants or equity for existing employees |
| `source_urls` | Space-separated |
| `quote` | The exact sentence for each non-blank answer |

Columns: `company, crunchbase_url, stock_type, exercise_window, vesting_schedule, tender_history, equity_refresh, source_urls, quote, checked_on, confidence`

Output: **`equity_terms.csv`**

### 1C. Published equity benchmarks

Find published figures for **equity granted to a mid-level and a senior software
engineer**, as a percentage of the company and/or as a dollar value. Record them by
company stage (seed, Series A, B, C, D+) and, if available, by company size or
employee number. Sources to check:

- Index Ventures' OptionPlan (US guidelines)
- Carta's compensation and equity reports
- The Holloway Guide to Equity Compensation
- Any other publication by a venture firm or compensation-data company that gives
  numbers, not just advice

Columns: `source, source_url, publication_date, stage, company_size_or_employee_number, role, level, equity_percent, equity_value_usd, quote, confidence`

Output: **`equity_benchmarks.csv`**

### Companies for Part 1

**Top 40 of the current list:**

| Rank | Company | Employees | Crunchbase |
|---|---|---|---|
| 1 | LiveKit | 101-250 | https://www.crunchbase.com/organization/livekit |
| 2 | Varda | 101-250 | https://www.crunchbase.com/organization/varda-ba64 |
| 3 | Serval | 101-250 | https://www.crunchbase.com/organization/serval-a045 |
| 4 | Solace | 101-250 | https://www.crunchbase.com/organization/solace-f37a |
| 5 | Thatch | 101-250 | https://www.crunchbase.com/organization/thatch-c9a5 |
| 6 | Muon Space | 251-500 | https://www.crunchbase.com/organization/muon-space |
| 7 | SiMa.ai | 101-250 | https://www.crunchbase.com/organization/sima-ai |
| 8 | Rain | 101-250 | https://www.crunchbase.com/organization/rain-855d |
| 9 | Upstage | 101-250 | https://www.crunchbase.com/organization/upstage-ai |
| 10 | ScaleOps | 101-250 | https://www.crunchbase.com/organization/scaleops-9685 |
| 11 | Turing | 1001-5000 | https://www.crunchbase.com/organization/turing |
| 12 | HappyRobot | 101-250 | https://www.crunchbase.com/organization/happyrobot |
| 13 | Pomelo Care | 251-500 | https://www.crunchbase.com/organization/pomelo-care |
| 14 | Deepgram | 251-500 | https://www.crunchbase.com/organization/deepgram |
| 15 | Cape | 101-250 | https://www.crunchbase.com/organization/private-tech |
| 16 | Reliable Robotics | 101-250 | https://www.crunchbase.com/organization/reliable-robotics |
| 17 | Exa | 101-250 | https://www.crunchbase.com/organization/exa-1b30 |
| 18 | Hightouch | 101-250 | https://www.crunchbase.com/organization/hightouch-0e87 |
| 19 | Blank Street | 101-250 | https://www.crunchbase.com/organization/blank-street |
| 20 | Doppel | 251-500 | https://www.crunchbase.com/organization/doppel-9e9d |
| 21 | Ledgebrook | 251-500 | https://www.crunchbase.com/organization/ledgebrook |
| 22 | Braintrust | 101-250 | https://www.crunchbase.com/organization/braintrust-data |
| 23 | TRM Labs | 251-500 | https://www.crunchbase.com/organization/trm-labs |
| 24 | Preply | 501-1000 | https://www.crunchbase.com/organization/preply |
| 25 | Fieldguide | 251-500 | https://www.crunchbase.com/organization/fieldguide |
| 26 | Encord | 101-250 | https://www.crunchbase.com/organization/cord-0d3f |
| 27 | Profound | 251-500 | https://www.crunchbase.com/organization/profound-1b0a |
| 28 | Standard Bots | 101-250 | https://www.crunchbase.com/organization/standard-bots |
| 29 | Gradial | 101-250 | https://www.crunchbase.com/organization/panorama-artificial-intelligence |
| 30 | Genius AI | 251-500 | https://www.crunchbase.com/organization/trygeniusai |
| 31 | Xona | 101-250 | https://www.crunchbase.com/organization/xona-space-systems |
| 32 | Assort Health | 101-250 | https://www.crunchbase.com/organization/assort-health |
| 33 | Neros Technologies | 101-250 | https://www.crunchbase.com/organization/neros-technologies |
| 34 | Omni | 101-250 | https://www.crunchbase.com/organization/omni-analytics |
| 35 | Firehawk Aerospace | 101-250 | https://www.crunchbase.com/organization/firehawk-aerospace |
| 36 | Port | 101-250 | https://www.crunchbase.com/organization/port-f926 |
| 37 | Snorkel AI | 251-500 | https://www.crunchbase.com/organization/snorkel-ai |
| 38 | Cornelis Networks | 101-250 | https://www.crunchbase.com/organization/cornelis-networks |
| 39 | Eon | 101-250 | https://www.crunchbase.com/organization/eon-e96e |
| 40 | Yassir | 501-1000 | https://www.crunchbase.com/organization/yassir |

**Size comparison set (Part 1A only).** These show whether smaller or larger
companies at similar valuations give bigger grants.

| Company | Employees | Valuation | Crunchbase |
|---|---|---|---|
| Daytona | 11-50 | $1.0B | https://www.crunchbase.com/organization/daytona-4480 |
| Town | 11-50 | $1.0B | https://www.crunchbase.com/organization/town-9f84 |
| Blacksmith | 11-50 | $1.0B | https://www.crunchbase.com/organization/blacksmith-fde4 |
| Goodfire | 11-50 | $1.3B | https://www.crunchbase.com/organization/goodfire-b4cb |
| Flow Engineering | 11-50 | $0.75B | https://www.crunchbase.com/organization/flowengineer |
| Eve | 51-100 | $1.0B | https://www.crunchbase.com/organization/eve-f25a |
| Nevis | 51-100 | $0.5B | https://www.crunchbase.com/organization/nevis-190a |
| Quartermaster AI | 51-100 | $0.77B | https://www.crunchbase.com/organization/quartermaster-ai |
| Patronus AI | 51-100 | $0.39B | https://www.crunchbase.com/organization/patronus-ai-61cd |
| Warp | 51-100 | $0.35B | https://www.crunchbase.com/organization/warp-e7b9 |
| Thyme Care | 501-1000 | $2.0B | https://www.crunchbase.com/organization/thyme-care |
| Farther | 501-1000 | $1.0B | https://www.crunchbase.com/organization/farther-finance |
| Tractian | 501-1000 | $1.4B | https://www.crunchbase.com/organization/tractian |
| Midi Health | 501-1000 | $1.0B | https://www.crunchbase.com/organization/midi-d939 |
| EvenUp | 501-1000 | $2.0B | https://www.crunchbase.com/organization/evenup |
| Kong | 1001-5000 | $2.0B | https://www.crunchbase.com/organization/konghq |
| Syntiant | 1001-5000 | $0.91B | https://www.crunchbase.com/organization/syntiant |
| Owner | 501-1000 | $2.3B | https://www.crunchbase.com/organization/owner-com |
| ID.me | 1001-5000 | $2.0B | https://www.crunchbase.com/organization/id-me |
| Coralogix | 501-1000 | $1.6B | https://www.crunchbase.com/organization/coralogix |
| Vestwell | 501-1000 | $2.0B | https://www.crunchbase.com/organization/vestwell |
| Axiom Space | 501-1000 | $2.5B | https://www.crunchbase.com/organization/axiom-space |

---

## Part 2 – Published research

For each item, record every relevant figure as its own row:

`question, source, source_url, publication_date, period_covered, metric, value, unit, breakdown, quote, confidence, notes`

Use `breakdown` for any split (year, cohort, stage, sector). Prefer the most recent
edition of each source, and also record older editions when they show a trend.

| question | What to find | Where to look first |
|---|---|---|
| `ipo_age` | Median age of companies at IPO, by year, for as many years as available (ideally 1980 to 2025), plus the number of venture-backed IPOs per year | Jay Ritter's IPO data, University of Florida (site.warrington.ufl.edu/ritter/ipo-data) |
| `time_to_exit` | Median years from first venture funding (or founding) to IPO or acquisition, by year | PitchBook-NVCA Venture Monitor, Carta State of Private Markets |
| `graduation_rates` | Share of seed-funded companies that go on to raise Series A, B, C and later, and how long it takes, by cohort year | Carta State of Private Markets, CB Insights venture funnel reports |
| `founder_outcomes` | How much founders typically own after each round, and the share of startups that shut down, by cohort | Carta founder ownership and shutdown reports |
| `common_vs_preferred` | How employee stock (common, valued by 409A) compares with what investors paid per share (preferred), e.g. 409A as a percentage of the preferred price, by stage | Carta 409A reports and blog posts |
| `investor_terms` | Share of venture deals with liquidation preferences above 1×, with participating preferences, and similar terms that put investors ahead of employees, by year | Cooley Venture Financing Report, Fenwick Silicon Valley Venture Survey, Carta |
| `tender_frequency` | How often private companies run employee tender offers, by stage, and what share of eligible employees sell | Carta tender offer reports, Nasdaq Private Market reports |

Output: **`published_benchmarks.csv`**

---

## Report back

- All five CSV files, pasted in full: `levels_grants.csv`, `equity_terms.csv`,
  `equity_benchmarks.csv`, `published_benchmarks.csv`, and a short `run_log.csv`
  listing gated pages, blocked sites and anything skipped
- A short summary: which questions have solid numbers, and which sources were gated
