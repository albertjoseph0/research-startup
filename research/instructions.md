# Browser agent task: save three Crunchbase searches for Albert's November export

Create three saved searches in Albert's Crunchbase account, with the exact filters and
columns below. **Do not export or download anything.** Albert will export them himself
from his laptop.

## Why these replace the 30 Oct searches

The two searches saved on 30 Oct ("Series B companies – 2025 onward", 843 rows, and
"Series C-F companies – under 101 employees", 269 rows) have three problems:

1. **Missing columns.** No columns were set, so they would export Crunchbase's default view.
   That view lacks fields the scoring needs: web visits growth, trend score, lead investors,
   layoff date, funding totals.
2. **Too many cheap companies.** The Nov 1 test of 2015–19 rounds found that companies priced
   low for their stage had the worst cash outcomes. Only 3% of $100M–300M Series C–E rounds
   reached a 5× cash exit, against 9% at $300M–1B and 22% at $1B–3B. Most of the 843 Series B
   companies raised small rounds at low prices.
3. **Too many rows to value.** Exports leave most valuations blank. Filling them through the
   Crunchbase connection costs about 60 tokens per company, and about 38,000 tokens are left
   this month, which covers roughly 600 companies. A funding-rounds export (Search 3) fills
   many valuations for free.

Leave the 30 Oct saved searches, and every other saved search, untouched.

---

## 0. Rules

1. The only changes allowed: create the three new saved searches and set their columns.
   Do not edit or delete other saved searches, alerts, lists or account settings.
2. Do not export, download, or click "Export".
3. Use Albert's existing signed-in browser session. If Crunchbase asks you to log in,
   stop and tell Albert. Do not enter credentials.
4. Do not contact anyone, start trials, or buy anything.
5. If a filter or column below doesn't exist under that name, use the closest one and write
   down exactly what you used.

---

## 1. Search 1: `Join pool – Series B, round $50M+ (Nov 2026)`

**Search → Companies.** Filters:

| Filter | Value |
|---|---|
| Headquarters location | United States |
| Operating status | Active |
| Company type | For profit |
| IPO status | Private |
| Last funding type | Series B |
| Last funding date | On or after 2025-01-01 |
| Number of employees | 11-50, 51-100, 101-250, 251-500, 501-1000, 1001-5000 |
| Last funding amount (USD) | $50,000,000 or more |

Why $50M: a Series B round of $50M or more usually means a price of roughly $250M–$400M or
higher. That leaves out the low-priced companies that did worst in the test. The real
valuation is checked later, so this filter is only a first cut.

Before saving, record the result count at each of these minimums. Change only the last
funding amount filter, then set it back to $50M before you save:

| Minimum | Count |
|---|---|
| none | |
| $30M | |
| $50M | |
| $75M | |
| $100M | |

## 2. Search 2: `Join pool – Series C-F, 11-100 employees, round $50M+ (Nov 2026)`

**Search → Companies.** Filters:

| Filter | Value |
|---|---|
| Headquarters location | United States |
| Operating status | Active |
| Company type | For profit |
| IPO status | Private |
| Last funding type | Series C, Series D, Series E, Series F |
| Last funding date | On or after 2024-11-01 |
| Number of employees | 11-50, 51-100 |
| Last funding amount (USD) | $50,000,000 or more |

This covers smaller late-stage companies. The earlier pool required 101+ employees, and that
cut-off has not been tested.

Record the count at no minimum (it should be about 269), $30M, $50M and $75M. Save the
search at $50M.

### Columns for Searches 1 and 2

Use **Edit View / Edit Columns** and set exactly these columns, in this order. Where a
column has a USD version ("... (in USD)"), Crunchbase adds it next to the original on export.
Keep the "... URL" columns, which the merge needs.

1. Organization Name (with Organization Name URL)
2. Number of Employees
3. Last Funding Date
4. Last Funding Type
5. IPO Status
6. Operating Status
7. Company Type
8. Stage
9. Industries
10. Headquarters Location
11. Description
12. CB Rank (Company)
13. Founded Date
14. Estimated Revenue Range
15. Actively Hiring
16. Last Funding Amount
17. Total Funding Amount
18. Number of Funding Rounds
19. Top 5 Investors
20. Lead Investors
21. Last Leadership Hiring Date
22. Last Layoff Mention Date
23. Trend Score (90 Days)
24. Monthly Visits
25. Average Visits (6 months)
26. Monthly Visits Growth
27. Downloads Last 30 Days
28. Growth Score Tier
29. Heat Score Tier

## 3. Search 3: `Join pool – Series B-C rounds with valuation, Jan 2025-Jun 2026`

**Search → Funding Rounds.** This fills valuations for Series B and C rounds that the
earlier exports didn't cover. Those exports were Series B–F rounds after 2026-07-01, and
Series D–F rounds from 2024-11-01 to 2026-06-30.

Filters:

| Filter | Value |
|---|---|
| Organization location (headquarters) | United States |
| Funding type | Series B, Series C |
| Announced date | 2025-01-01 to 2026-06-30 |
| Post-money valuation (USD) | $1 or more, so that only rounds with a disclosed valuation are kept |

Columns, in this order:

1. Transaction Name (with Transaction Name URL)
2. Organization Location
3. Organization Name (with Organization Name URL)
4. Funding Type
5. Money Raised
6. Announced Date
7. Post-Money Valuation
8. Lead Investors

**Counts to record:**
- the count with the valuation filter;
- the count without it (remove the filter, read the count, then put it back before saving).

If there is no valuation filter, save the search without it and say so.

---

## 4. Row budget check

Albert can export 2,000 rows this month. Add up Search 1 (at $50M), Search 2 (at $50M) and
Search 3.

- **Total 1,800 or under:** keep all three as saved.
- **Total over 1,800:** first change Search 1's minimum to $75M and save again.
- **Still over 1,800:** also change Search 2's minimum to $75M.
- **Record** which minimums the saved versions ended with.

---

## 5. Output: `saved_searches_v2.csv`

Columns:

| Column | What to record |
|---|---|
| `search_name` | |
| `url` | the saved search's link |
| `entity` | `companies` or `funding rounds` |
| `filters_set` | each filter and value, as actually set |
| `result_count` | count of the saved version |
| `counts_at_other_minimums` | e.g. `none=843; 30M=...; 50M=...; 75M=...; 100M=...` |
| `columns_set_ok` | `yes`, or the list of columns missing or renamed |
| `filters_not_set_exactly` | any filter you couldn't set as written, and what you used instead |
| `checked_on` | today's date |

**Final message:** the three links, their row counts, the total, and whether anything was
set differently from these instructions.
