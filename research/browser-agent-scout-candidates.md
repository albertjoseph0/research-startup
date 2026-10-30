# Browser agent: check 49 new candidate companies

The Crunchbase homepage assistant suggested 49 companies that are not yet in the user's
company list. They are mostly companies whose latest funding round was a Series B or C,
reportedly valued $300M–$1.5B. Each needs to be checked and its key facts recorded
in the same format as the existing list, so it can be scored alongside the others.

Do Part A for all 49 companies first, then Part B.

---

## Rules

1. **Visit only the 49 Crunchbase profile URLs listed below,** one at a time, at a
   normal reading pace. Don't use Advanced Search, don't export, and don't open other
   companies' profiles.
2. **If Crunchbase shows a CAPTCHA, a warning, or a usage-limit message, stop
   immediately** and report it word for word.
3. **Work in batches of 10 companies.** After each batch, paste that batch's rows for
   both CSV files into your reply, so nothing is lost if the browser crashes.
4. **Copy values exactly as Crunchbase shows them.** Leave a cell blank if the profile
   doesn't show the value. Never estimate.
5. **If a profile is for an obviously different company** than the name given (for
   example a different industry, or the URL redirects), record what the profile shows
   and explain in `notes`.

---

## Part A – Crunchbase profile facts

For each company, open its profile and look at the Overview and Financials sections.
Look at the technology or web-traffic section too, if the profile has one.

### File 1: `scout_companies.csv`

One row per company. Use exactly these column names:

| Column | What to record |
|---|---|
| Organization Name | Name as shown on the profile |
| Organization Name URL | The profile URL from the list below |
| Number of Employees | The employee range as shown, e.g. `101-250` |
| Last Funding Date | Date of the most recent funding round, `YYYY-MM-DD` |
| Last Funding Type | e.g. `Series B` |
| IPO Status | e.g. `Private` |
| Operating Status | e.g. `Active` |
| Company Type | e.g. `For-profit` |
| Industries | As listed, comma-separated |
| Headquarters Location | e.g. `San Francisco, California, United States` |
| Description | The short description |
| CB Rank (Company) | Number, if shown |
| Founded Date | `YYYY-MM-DD` (or the year if only that is shown) |
| Estimated Revenue Range | e.g. `$10M to $50M`, if shown |
| Total Funding Amount (in USD) | Number, no `$` or commas |
| Number of Funding Rounds | Number |
| Top 5 Investors | Comma-separated |
| Lead Investors | Comma-separated, from the latest round |
| Last Layoff Mention Date | `YYYY-MM-DD`, if any layoff is shown |
| Trend Score (90 Days) | Number, if shown |
| Monthly Visits | Number, if shown |
| Average Visits (6 months) | Number, if shown |
| Monthly Visits Growth | e.g. `12.5%`, if shown |
| notes | Anything odd: renamed company, mismatched profile, missing sections |

### File 2: `scout_rounds.csv`

From the funding rounds table, record **every round announced on or after
2024-01-01**, plus the **one round just before that** (so step-ups can be measured).
One row per round:

| Column | What to record |
|---|---|
| Transaction Name URL | The round's own Crunchbase link if shown; otherwise `<profile URL>#<round type>#<date>` |
| Organization Name | As in File 1 |
| Organization Name URL | As in File 1 |
| Funding Type | e.g. `Series B` |
| Announced Date | `YYYY-MM-DD` |
| Money Raised (in USD) | Number, blank if undisclosed |
| Post-Money Valuation (in USD) | Number, blank if not shown |
| Valuation Source | `Confirmed` or `Estimated`, exactly as Crunchbase labels the valuation; blank if no valuation |

### Companies (49)

| # | Name | Crunchbase profile |
|---|---|---|
| 1 | Infisical | https://www.crunchbase.com/organization/infisical |
| 2 | Nevis | https://www.crunchbase.com/organization/nevis-190a |
| 3 | Formic | https://www.crunchbase.com/organization/formic |
| 4 | Daytona | https://www.crunchbase.com/organization/daytona-4480 |
| 5 | Town | https://www.crunchbase.com/organization/town-9f84 |
| 6 | Blacksmith | https://www.crunchbase.com/organization/blacksmith-fde4 |
| 7 | Stand | https://www.crunchbase.com/organization/stand-8e17 |
| 8 | Cellbri | https://www.crunchbase.com/organization/cellbri |
| 9 | Omaha Productions | https://www.crunchbase.com/organization/omaha-productions |
| 10 | Epicrispr Biotechnologies | https://www.crunchbase.com/organization/epic-bio |
| 11 | Character Biosciences | https://www.crunchbase.com/organization/clover-therapeutics |
| 12 | Hammerspace | https://www.crunchbase.com/organization/hammerspace-4936 |
| 13 | Crux | https://www.crunchbase.com/organization/crux-70b8 |
| 14 | Parallel Systems | https://www.crunchbase.com/organization/parallel-systems-1d43 |
| 15 | Eve | https://www.crunchbase.com/organization/eve-f25a |
| 16 | Vibe | https://www.crunchbase.com/organization/vibe-970b |
| 17 | Valence | https://www.crunchbase.com/organization/valence-5e27 |
| 18 | Factory | https://www.crunchbase.com/organization/factory-19d8 |
| 19 | Zus Health | https://www.crunchbase.com/organization/zus-health |
| 20 | Kargo | https://www.crunchbase.com/organization/kargo-ae46 |
| 21 | Atavistik Bio | https://www.crunchbase.com/organization/atavistik-bio |
| 22 | Aeovian Pharmaceuticals | https://www.crunchbase.com/organization/aeonian-pharmaceuticals |
| 23 | Chai Discovery | https://www.crunchbase.com/organization/chai-discovery |
| 24 | Zocks | https://www.crunchbase.com/organization/zocks |
| 25 | Braintrust | https://www.crunchbase.com/organization/braintrust-data |
| 26 | Overland AI | https://www.crunchbase.com/organization/overland-ai |
| 27 | BrainCo | https://www.crunchbase.com/organization/brainco |
| 28 | Goodfire | https://www.crunchbase.com/organization/goodfire-b4cb |
| 29 | Xenter | https://www.crunchbase.com/organization/xenter |
| 30 | Patronus AI | https://www.crunchbase.com/organization/patronus-ai-61cd |
| 31 | Warp | https://www.crunchbase.com/organization/warp-e7b9 |
| 32 | Captura | https://www.crunchbase.com/organization/captura |
| 33 | Ollin Biosciences | https://www.crunchbase.com/organization/ollin-biosciences |
| 34 | Flow Engineering | https://www.crunchbase.com/organization/flowengineer |
| 35 | Miter | https://www.crunchbase.com/organization/miter-057c |
| 36 | Efficient Computer | https://www.crunchbase.com/organization/efficientai |
| 37 | Reco | https://www.crunchbase.com/organization/reco-67bb |
| 38 | Quartermaster AI | https://www.crunchbase.com/organization/quartermaster-ai |
| 39 | Persefoni AI | https://www.crunchbase.com/organization/persefoni |
| 40 | Navina | https://www.crunchbase.com/organization/navina |
| 41 | Decagon | https://www.crunchbase.com/organization/decagon-485e |
| 42 | Flexiv | https://www.crunchbase.com/organization/flexiv |
| 43 | LuxWall | https://www.crunchbase.com/organization/luxwall |
| 44 | Last Energy | https://www.crunchbase.com/organization/last-energy |
| 45 | Culture Biosciences | https://www.crunchbase.com/organization/culture-robotics |
| 46 | Terrestrial Bio | https://www.crunchbase.com/organization/vaxess-technologies |
| 47 | Cents | https://www.crunchbase.com/organization/cents-ba2f |
| 48 | Higharc | https://www.crunchbase.com/organization/higharc |
| 49 | Flare Therapeutics | https://www.crunchbase.com/organization/flare-therapeutics |

Notes: #46's link points to a profile named Vaxess Technologies, which may be a rename;
confirm which company the profile is. #22's link spells the name "Aeonian"; this is
probably the same company.

---

## Part B – Open-web research (only for companies that pass these checks)

After Part A, take only the companies where **all** of these are true in File 1:
- headquarters in the United States;
- Operating Status is Active and IPO Status is Private;
- Number of Employees is 101-250 or larger;
- the latest round in File 2 has a post-money valuation between $300M and $1.5B.

For those, do the same three checks as the earlier research round. Use **the same
column names as before**, and put each company's Crunchbase profile URL in
`crunchbase_url`:

1. **`scout_job1_hiring.csv`:** open roles now on the company's careers page, found by
   following the careers link on its homepage (never guess job-board addresses). Also
   record open software engineering roles (backend, platform, infrastructure, systems,
   data; no front-end-only, mobile-only, QA-only or IT support), and the count from the
   Wayback Machine 6 and 12 months ago if an archived copy renders.
   Columns: `company, crunchbase_url, careers_url, job_board, open_roles_now, open_roles_target_role_now, open_roles_6mo_ago, snapshot_6mo_date, open_roles_12mo_ago, snapshot_12mo_date, checked_on, confidence, notes`
2. **`scout_job2_revenue.csv`:** the most recent revenue or ARR figure stated by the
   company or a reputable outlet (not estimate sites).
   Columns: `company, crunchbase_url, revenue_usd, revenue_type, as_of_date, growth_statement, source_url, checked_on, confidence`
3. **`scout_job3_liquidity.csv`:** employee tender offers in the last 24 months, IPO
   filings, and acquisitions or mergers. Write `None found` where nothing is found.
   Columns: `company, crunchbase_url, tender_offer_date, tender_offer_valuation_usd, tender_offer_details, secondary_price_valuation_usd, secondary_price_date, secondary_source, ipo_signal, ipo_signal_date, acquisition_signal, source_urls, checked_on, confidence`

For Part B searches, use DuckDuckGo or Bing; Google blocks automated searches. Do not
log in to or browse LinkedIn, Glassdoor or Blind.

---

## Report back

- All five CSV files, pasted in full
- Which companies failed the Part B checks, and why
- Any profile that didn't match its name, and any CAPTCHA, warning or limit message
