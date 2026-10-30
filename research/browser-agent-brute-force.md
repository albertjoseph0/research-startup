# Browser agent – brute-force research on every candidate company

You are researching every company in `company_universe.csv` (374 private US companies
whose last round was a Series C–F), and then looking for good candidates the list
missed. The user's goal is to join a company where an employee's equity can produce a
**large payoff that turns into cash within about 4 years**. Exports are used up, so all
of this work uses page visits and open sources.

You have plenty of time. Be thorough, and prefer accuracy to speed. Read the whole
document before starting.

---

## 0. Ground rules

1. **No Crunchbase bulk collection.** Do not page through Crunchbase search results to
   copy rows, and do not visit Crunchbase profiles in bulk. Doing either works around
   the export limit and breaks Crunchbase's terms, which risks the user's account.
   Crunchbase valuation data will be filled through the user's API connection after
   2026-11-01.
2. **No LinkedIn, Glassdoor or Blind in this round.** These sites ban automated
   browsing and suspend accounts. The shortlist checks you are already running are
   the only exception.
3. **Do not create accounts, log in to new sites, accept paid trials, or submit any
   form.** Read only. Do not contact companies, message people, or apply to jobs.
4. **Every value needs a source URL.** If a reputable source can't be found, write
   `None found`. Never estimate or guess. Reputable means: the company's own site or
   press release, SEC filings, Bloomberg, Reuters, WSJ, FT, The Information,
   TechCrunch, Axios, Forbes, CNBC, Business Insider, Fortune, or official public data
   pages (Wayback Machine, job boards run by the company's applicant-tracking system).
5. **Be polite to websites.** Use one tab per site at a time and pause between page
   loads, as a person would. If a site shows a CAPTCHA, a rate-limit message or a
   block, stop using that site and note it in `run_log.csv`.
6. **Save progress often.** Write results to each job's CSV file after every 25
   companies, so that work can resume after an interruption. Skip companies that
   already have a row.
7. **Process companies in `priority` order** (1 = most promising). If time runs short,
   the top of the list matters most.
8. **Key every row by `company` and `crunchbase_url`, copied exactly** from
   `company_universe.csv`. Add `checked_on` (date) and `confidence` (`high` / `medium`
   / `low`) to every row.
9. Jobs 1–6 are independent. If you can run several sessions, run them in parallel.

---

## Job 1 – Hiring momentum (all 374 companies)

Hiring speed is the best free stand-in for growth. Count open jobs now and in the past.

1. Find the company's careers page from its website. Identify the job-board provider
   from the careers page links. Common providers are Greenhouse
   (`boards.greenhouse.io/<name>` or `job-boards.greenhouse.io/<name>`), Lever
   (`jobs.lever.co/<name>`), Ashby (`jobs.ashbyhq.com/<name>`), Workday, Rippling and
   Workable.
2. Count today's open roles. Count all of them, and separately count roles matching the
   user's target role: _fill in, e.g. "software engineer"_.
3. In the Wayback Machine (`web.archive.org/web/*/<careers page URL>`), open the
   snapshot closest to **2026-04-30** and the one closest to **2025-10-30**. Count the
   open roles in each. If a snapshot doesn't show the job list (for example, it loaded
   by script), try the job-board URL itself in the Wayback Machine. If neither works,
   write `None found`.

Output **`job1_hiring.csv`** with these columns: `company`, `crunchbase_url`,
`careers_url`, `job_board`, `open_roles_now`, `open_roles_target_role_now`,
`open_roles_6mo_ago`, `snapshot_6mo_date`, `open_roles_12mo_ago`,
`snapshot_12mo_date`, `checked_on`, `confidence`, `notes`.

---

## Job 2 – Revenue and ARR (all 374 companies)

The goal is a valuation-to-revenue multiple, which shows how much of the future is
already priced in.

For each company, search news for the **most recent** public revenue or ARR figure
(search terms: `"<company>" ARR`, `"<company>" annual recurring revenue`,
`"<company>" revenue run rate`, `"<company>" revenue 2026`). Record only figures stated
by the company or reported by a reputable outlet. "Doubled revenue" with no figure
goes in `growth_statement`, not in `revenue_usd`.

Output **`job2_revenue.csv`** with these columns: `company`, `crunchbase_url`,
`revenue_usd` (number, e.g. `200000000`), `revenue_type` (`ARR` / `run-rate` /
`annual revenue`), `as_of_date`, `growth_statement` (quote any stated growth rate,
e.g. "3x year over year"), `source_url`, `checked_on`, `confidence`.

---

## Job 3 – Early cash and IPO signals (all 374 companies)

This is the most important job for the user's goal.

For each company, search for:

- **Employee tender offers or secondary sales** in the last 24 months
  (`"<company>" tender offer`, `"<company>" secondary sale employees`). Record date,
  size, price or valuation, and who bought.
- **Secondary-market prices** shown on **public, logged-out** pages (Forge Price,
  EquityZen, Hiive, Caplight, Notice). Record the indicative price or implied
  valuation and its date. Do not sign up to see more.
- **IPO signals** in the last 12 months: statements about IPO timing, a confidential
  S-1 filing, bank hires, or a new CFO/general counsel who has taken a company public
  before.
- **Acquisition signals:** credible reports of the company being acquired or in talks.

Output **`job3_liquidity.csv`** with these columns: `company`, `crunchbase_url`,
`tender_offer_date`, `tender_offer_valuation_usd`, `tender_offer_details`,
`secondary_price_valuation_usd`, `secondary_price_date`, `secondary_source`,
`ipo_signal` (short description or `None found`), `ipo_signal_date`, `acquisition_signal`,
`source_urls` (space-separated), `checked_on`, `confidence`.

---

## Job 4 – SEC Form D filings (all 374 companies)

US companies that sell shares in private rounds usually file a Form D with the SEC. It
is public and free, and it can reveal rounds that haven't been announced yet.

1. Search EDGAR company search (`https://www.sec.gov/cgi-bin/browse-edgar?company=<name>&type=D`)
   or EDGAR full-text search (`https://efts.sec.gov/LATEST/search-index?q="<name>"&forms=D`).
   Companies often file under their legal name (e.g. "Xona Space Systems Inc."), so
   check the company website footer or terms page for the legal name if needed.
2. Open the **two most recent** Form D or D/A filings.
3. From each, record: filing date, date of first sale, total offering amount, total
   amount sold, number of investors, and security type (equity, option, debt).

SEC asks automated visitors to stay under 10 requests per second; stay far below that.
If a company can't be matched with confidence, write `None found`, not a guess.

Output **`job4_formd.csv`** with these columns: `company`, `crunchbase_url`,
`legal_name`, `cik`, `filing_date`, `first_sale_date`, `total_offering_usd`,
`total_sold_usd`, `num_investors`, `security_type`, `filing_url`. Use one row per
filing, at most 2 per company. Add `checked_on` and `confidence`.

---

## Job 5 – Product traction (all 374 companies, one metric per company)

Choose the **one** metric that fits the company's business, and record its value now
and about 12 months ago:

| Business type | Metric | Where |
|---|---|---|
| Developer tool or open-source product | GitHub stars of the main repo | GitHub repo page plus `star-history.com` |
| Consumer app | App Store / Google Play chart rank or rating count | Public store pages; Wayback Machine for the past value |
| Consumer or SMB website | Monthly visits | Similarweb public overview page (logged out) |
| Enterprise software | Customer count or named logos, as stated by the company | Company site, press releases, Wayback Machine for the past value |
| Hardware, space, biotech, defense | Contracts won, launches, regulatory milestones in the last 12 months | Press releases, government contract announcements |

Output **`job5_traction.csv`** with these columns: `company`, `crunchbase_url`,
`metric`, `value_now`, `value_now_date`, `value_12mo_ago`, `value_12mo_date`,
`source_urls`, `checked_on`, `confidence`, `notes`.

---

## Job 6 – Equity compensation data (priority 1–60 only)

For each company, open its public Levels.fyi company page (logged out, read only).
For the user's target role, record the median total compensation, the median yearly
stock value and the number of data points. If there are fewer than 3 data points,
record what's shown and set confidence to `low`.

Output **`job6_comp.csv`** with these columns: `company`, `crunchbase_url`, `role`,
`level` (if shown), `median_total_comp_usd`, `median_stock_per_year_usd`,
`data_points`, `source_url`, `checked_on`, `confidence`.

---

## Job 7 – Find companies the list missed (after Jobs 1–6, or in parallel)

The Crunchbase screen depended on Crunchbase's own data, which has gaps. Build a
candidate list from public rankings and investor portfolios:

- Forbes AI 50 (2025 and 2026), Forbes Cloud 100 (2025 and 2026), CNBC Disruptor 50
  (2025 and 2026)
- The public portfolio pages of: Sequoia Capital, Andreessen Horowitz, Benchmark,
  Accel, Founders Fund, Lightspeed, Index Ventures, Greylock, Kleiner Perkins,
  General Catalyst, Thrive Capital, Khosla Ventures, Redpoint, Bessemer
- Y Combinator's public "top companies" list

Keep a company only if **all** of these are true and confirmed by a reputable source:
- It is headquartered in the US and still private.
- Its most recent priced round was a Series C, D, E or F, announced on or after 2024-11-01.
- Its last reported valuation is $10B or less.
- It has more than 100 employees, based on a company statement or a reputable article.
- It is **not** already in `company_universe.csv`. Check by name and website.

Output **`job7_new_candidates.csv`** with these columns: `company`, `website`,
`found_via`, `last_round`, `last_round_date`, `last_round_size_usd`,
`last_valuation_usd`, `employees_statement`, `description`, `source_urls`,
`checked_on`, `confidence`.

Then run Jobs 1–5 on the new candidates as well. Use `website` as their key in place
of `crunchbase_url`.

---

## Job 8 – Final quality check (last)

Pick 20 random rows from each output file and re-verify them against their sources.
Record the error rate per file in `run_log.csv`. If a file's error rate is above 10%,
re-check every row in that file whose confidence is `medium` or `low`.

---

## What to hand back

All `jobN_*.csv` files plus `run_log.csv`, which records sites that blocked you, rows
skipped, error rates from Job 8, and deviations from these instructions. Then report:

1. Rows completed per job.
2. The 10 companies with the strongest early-cash signals (tender offers, secondary
   prices above the last round, credible IPO plans).
3. The 10 companies with the fastest hiring growth over 12 months.
4. Any company where the evidence contradicts the Crunchbase data (for example a
   Form D showing a raise Crunchbase doesn't list, or layoffs Crunchbase missed).
