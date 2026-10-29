# Instructions for the browser agent: build a ranked list of companies to join

You are working in the user's browser with their logged-in Crunchbase account. Your job is
to produce a ranked shortlist of private companies that a talented person should join as
an employee to maximise the chance of a large equity payoff **that turns into cash within
about 4 years**. Work through the phases in order. Read the whole document before starting.

---

## 0. User settings (the user edits these before handing off)

| Setting | Value |
|---|---|
| Headquarters location | United States |
| Sectors to include | Any |
| Sectors to exclude | None |
| Output | A Google Sheet in the user's Google Drive named `Company screen – <YYYY-MM>` |
| Export budget this month | 2,000 rows (hard limit, shared by every export) |

If a setting is blank, use the default shown.

---

## 1. Why the filters are what they are (do not change them without a reason)

These rules come from a study of US companies that raised Series A–E rounds in 2015–2019
and what happened to them afterwards:

- **Later stage gets to cash faster.** Within 4 years of the round, 9% of Series A companies
  had exited (IPO or acquisition), against 24% at Series D and 33% at Series E.
- **Large cashed-out gains came mostly from late stage.** A 5× gain realised within
  4 years happened to about 1% of Series A–C companies and 5–6% of Series D–E companies.
- **Early stage looks better only on paper.** Series A had the best paper multiples
  but the worst cash outcomes, because most of that value stays locked up for years.
- **Stage alone is not enough.** Even at Series E the odds are low, so the ranking in
  Phase 4 does most of the work.
- **Caveat:** part of the D/E advantage may come from the 2020–21 IPO boom. That is why
  Series C stays in as a second tier rather than being dropped.

---

## 2. Rules you must follow

1. **Never exceed the export budget.** Before every export, read the result count shown
   by Crunchbase. If it is larger than the row allowance for that export (below),
   narrow the search first, as described, and re-check. Never export "just to see".
2. **Log every export** in the `export_log` tab: date, search type, every filter used,
   sort order, row count exported, and rows remaining in the month's budget.
3. **Viewing pages is free; exporting is not.** Use exports for breadth (the full screen)
   and visits to individual company profiles for depth (the shortlist only).
4. **Do not** buy anything, change the plan, change account settings, contact any company,
   apply to jobs, or save searches/lists other than the ones named here.
5. **If the interface differs from these instructions** (a filter or column is missing or
   named differently), use the closest equivalent and note the substitution in
   `export_log`. If no reasonable equivalent exists for a **filter**, stop and ask the user.
   For a missing **column**, skip it and carry on.
6. Do not invent data. Leave a cell blank when Crunchbase has no value.

---

## 3. Phase 1 – Main screen export (allowance: up to 1,200 rows)

Go to Crunchbase **Search → Companies** (Advanced Search) and apply these filters:

| Filter | Value |
|---|---|
| Headquarters location | Setting from section 0 |
| Operating status | Active |
| Company type | For profit |
| IPO status | Private |
| Last funding type | Series C, Series D, Series E, Series F |
| Last funding date | On or after 2024-11-01 |
| Number of employees | 101–250, 251–500, 501–1000, 1001–5000 |
| Industries | Settings from section 0 (only if the user set them) |

**If the result count exceeds 1,200**, narrow it in this order and re-check after each step
until the count fits:
1. Last funding date on or after 2025-05-01.
2. Remove the 101–250 employee band.
3. Remove Series C (record this prominently in `export_log`, because it removes the hedge
   described in section 1).

**Sort:** CB Rank (Company), best first.

**Columns** – edit the table columns to include as many of these as are available, then export
to CSV:

- Organization Name, Organization Name URL, Description, Industries, Headquarters Location
- Founded Date, Number of Employees
- Last Funding Type, Last Funding Date, Last Funding Amount, Total Funding Amount,
  Number of Funding Rounds
- Top 5 Investors, Lead Investors
- Estimated Revenue Range, Most Recent Valuation Range
- CB Rank (Company), Trend Score (90 Days), Growth Score, Heat Score
- Monthly Visits, Monthly Visits Growth, Average Visits (6 months)
- Downloads Last 30 Days, Monthly Download Growth
- Actively Hiring, Last Layoff Mention Date, Last Leadership Hiring Date
- IPO Prediction Tier, Acquisition Prediction Tier

Import the CSV into the Google Sheet as the tab `raw_companies`.

---

## 4. Phase 2 – Valuation history export (allowance: up to 500 rows, optional)

Run this only if Phase 1 used 1,200 rows or fewer **and** at least 800 rows remain.

Go to **Search → Funding Rounds** and apply:

| Filter | Value |
|---|---|
| Organization location | Setting from section 0 |
| Funding type | Series B, Series C, Series D, Series E, Series F |
| Announced date | On or after 2022-01-01 |
| Post-money valuation | Not blank (any value) |

If the count exceeds 500, move the announced date forward six months at a time until it fits.

**Columns:** Organization Name, Transaction Name, Funding Type, Announced Date,
Money Raised, Post-Money Valuation, Lead Investors. Export and import as tab `raw_rounds`.

If you skip this phase, record why in `export_log`; Phase 5 will collect valuations
for the shortlist from profile pages instead.

**Keep at least 300 rows unexported** as a reserve for fixing a mistaken export.

---

## 5. Phase 3 – Hard gates (in the sheet, no Crunchbase usage)

Create tab `scored` from `raw_companies`. Mark each company **EXCLUDED** (with the reason)
if any of these is true:

1. Last Layoff Mention Date is on or after 2025-11-01.
2. Latest known valuation is above $10B, using `raw_rounds` if available, otherwise the
   Most Recent Valuation Range. A 5× gain would then need a $50B+ outcome.
3. Industries match an exclusion in section 0.

Add a column `tier`: **Tier 1** = last funding type Series D, E or F; **Tier 2** = Series C.

---

## 6. Phase 4 – Score the remaining companies (in the sheet)

For each signal below, compute the company's **percentile rank** (0–1) among the non-excluded
companies. Treat a blank as 0.5 (neutral), so missing data neither helps nor hurts.
Then compute the weighted score:

| Signal | How to compute | Weight |
|---|---|---|
| Web momentum | Average of the percentiles of Monthly Visits Growth and (Monthly Visits ÷ Average Visits (6 months)) | 20% |
| Crunchbase momentum | Percentile of Trend Score (90 Days) | 10% |
| Funding pace | From `raw_rounds`: months between the last two rounds (shorter is better). Without `raw_rounds`: Number of Funding Rounds ÷ years since Founded Date | 15% |
| Valuation step-up | From `raw_rounds`: latest post-money ÷ previous post-money. Without it: blank (0.5) | 10% |
| Room to grow | Latest valuation: $300M–$3B = 1.0; $3B–$10B = 0.5; under $300M = 0.6; unknown = 0.5 | 15% |
| Liquidity outlook | IPO Prediction Tier high = 1.0, medium = 0.6, low = 0.2; add 0.2 if revenue ≥ $100M (cap at 1.0) | 10% |
| Investor quality | 1.0 if any Lead Investor or Top 5 Investor is on the list below, else 0 | 10% |
| Hiring | 1.0 if Actively Hiring is populated, else 0 | 10% |

**Investor list:** Sequoia Capital, Andreessen Horowitz, Benchmark, Accel, Founders Fund,
Lightspeed Venture Partners, Index Ventures, Greylock, Kleiner Perkins, General Catalyst,
Thrive Capital, Coatue, ICONIQ Growth, Insight Partners, Khosla Ventures, Redpoint,
Bessemer Venture Partners, IVP, Tiger Global, Y Combinator.

`final_score = weighted score × (1.0 for Tier 1, 0.85 for Tier 2)`

Sort `scored` by `final_score`, highest first.

---

## 7. Phase 5 – Check the top 40 by hand (profile visits, no exports)

Open each of the top 40 company profiles on Crunchbase and record in tab `top_40`:

- Latest post-money valuation and date (from the funding rounds section), if not already known
- The previous round's valuation, to fill in the valuation step-up when `raw_rounds` was skipped
- Any news on the profile from the last 6 months about layoffs, down rounds, lawsuits,
  executive departures, or a planned IPO
- The 5× check: write `5 × latest valuation` and whether that outcome is plausible
  within 4 years (yes / stretch / no, with one sentence why)
- One sentence on what the company does and why it might become very large

Recompute the score for any company whose valuation or step-up changed, then re-sort.

---

## 8. Phase 6 – Deliverable

Finish the Google Sheet with tabs: `top_25`, `top_40`, `scored`, `raw_companies`,
`raw_rounds` (if run), `export_log`.

`top_25` columns: rank, company (linked to its Crunchbase page), tier, final score,
latest valuation, last round and date, employees, 5× check, two-line rationale,
main risk.

Then report back to the user with:
1. The link to the sheet.
2. Rows exported this month and rows remaining.
3. Every filter substitution or skipped phase, and why.
4. The 5 companies you would look at first, and one sentence each on why.

---

## 9. Lessons from the first run (2026-10-29)

- Most Recent Valuation Range, IPO Prediction Tier and Acquisition Prediction Tier are
  visible but blocked from export. Do not add them to export columns.
- Actively Hiring was blank for almost every company; Growth/Heat Score export only as tiers.
- The Phase 2 rounds search returned 5,718 rows from 2022, so it had to be cut to rounds
  after 2026-07-01, which gave valuations for only 93 of 406 companies. Prefer collecting
  valuations for the shortlist from profile pages (Phase 5) over a narrow rounds export.
- Scoring (Phases 3–4) is done by `research/score_companies.py`, not in the sheet.

## 10. Next month (after the export allowance resets)

Re-run Phase 1 with **Last funding date** on or after the date of the previous run,
to pick up only newly funded companies. Merge these into `raw_companies`, re-score,
and append a dated note to `export_log`. Spend any remaining budget on Phase 2 if it
was skipped.
