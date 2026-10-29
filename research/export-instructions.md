# Crunchbase export instructions (for a browser agent)

You are exporting three datasets from Crunchbase (crunchbase.com, already logged in) as CSV
files. Do not change account settings, upgrade plans, buy anything, or contact anyone.

## Rules for every export

1. Crunchbase exports at most 1,000 rows per file. Before each export, read the result count
   shown above the results table. If it is over 1,000, split the date window in half and
   export each half separately. Never export a search showing more than 1,000 results.
2. Set the columns listed below with "Edit View" / "Edit Columns" before the first export of
   each dataset, then reuse the same search and only change the date filter. Where a money
   column has a USD-converted version ("... (in USD)"), choose it. Always include the
   "... URL" column that sits next to each name column; it is the join key.
3. Name each file exactly as shown (e.g. `rounds_2015H1.csv`) and save it to the Google
   Drive folder `crunchbase-exports` (create it if missing).
4. After each export, open the CSV and confirm its row count equals the count Crunchbase
   showed. Record it in a file `manifest.csv` in the same folder with columns:
   `file,date_from,date_to,rows_shown,rows_in_file`.
5. If you see a message about an export or row limit, stop and report it. Do not continue.
6. Do the first export of each dataset, check its columns against the list, then do the rest.

## Dataset 1 — Entry funding rounds (expected total ≈ 11,395 rows)

Search type: **Funding Rounds**

Filters:
- Organization Location: **United States**
- Funding Type: **Series A, Series B, Series C, Series D, Series E**
- Post-Money Valuation: **greater than $0** (i.e. not blank)
- Announced Date: one window at a time, see below

Columns:
Transaction Name, Transaction Name URL, Organization Name, Organization Name URL,
Funding Type, Announced Date, Money Raised (in USD), Pre-Money Valuation (in USD),
Post-Money Valuation (in USD), Lead Investors, Number of Investors, Organization Industries,
Organization Location, Funding Status, Total Funding Amount (in USD)

Windows: calendar quarters (about 570 rows each), 20 files:
2015-01-01→2015-03-31 `rounds_2015Q1.csv`, 2015-04-01→2015-06-30 `rounds_2015Q2.csv`,
… through 2019-10-01→2019-12-31 `rounds_2019Q4.csv`.

## Dataset 2 — Acquisitions (expected total ≈ 14,493 rows)

Search type: **Acquisitions**

Filters:
- Acquiree Headquarters Location: **United States**
- Announced Date: one window at a time, from 2015-01-01 through today
- Acquiree Last Funding Type: Series A, B, C, D, E, F, G, H, I, J, Venture - Series Unknown,
  Private Equity, Corporate Round, Debt Financing, Convertible Note, Secondary Market,
  Undisclosed

Columns:
Transaction Name, Transaction Name URL, Acquiree Name, Acquiree Name URL, Acquirer Name,
Acquirer Name URL, Announced Date, Completed On Date, Price (in USD), Acquisition Type,
Acquisition Terms, Acquisition Status, Acquiree Last Funding Type,
Acquiree's Total Funding Amount (in USD), Acquiree Headquarters Location,
Acquiree Industries

Windows: half-years (about 600 rows each), `acq_2015H1.csv` … `acq_2026H2.csv`.
Split into quarters if any half-year is over 1,000.

## Dataset 3 — IPOs (expected total ≈ 4,271 rows)

Search type: **IPOs**

Filters:
- Stock Exchange: **NASDAQ, NYSE, NYSE American**
- IPO Date: one window at a time, from 2015-01-01 through today

Columns:
Organization Name, Organization Name URL, Stock Symbol, Stock Exchange, IPO Date,
Valuation at IPO (in USD), Amount Raised (in USD), Share Price at IPO (in USD),
Listing Type, Delisted Date

Windows: calendar years, `ipo_2015.csv` … `ipo_2026.csv`. 2020 and 2021 will likely be
over 1,000 because of SPAC listings; split those into half-years or quarters.

## When finished

Report: the number of files per dataset, the total rows per dataset (compare with the expected
totals above; a gap of more than ~5% means something was missed), and any columns you could
not find.
