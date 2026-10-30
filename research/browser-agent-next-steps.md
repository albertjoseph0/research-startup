# Browser agent – round 2: fill the valuation gaps and check the shortlist

You did the first pass already (company export, funding-rounds export, top-40 profile
checks). The user's analyst re-scored everything. This round fixes the biggest weakness
in the data and adds the checks that matter most for the user's goal: **a large equity
payoff that turns into cash within about 4 years**.

Read the whole document before starting. Do the parts in order.

---

## 0. Settings and budget

| Setting | Value |
|---|---|
| User's target role (for Part C) | _fill in, e.g. "senior backend engineer"_ |
| Crunchbase exports used this month | 1,470 of 2,000 → **530 left** |
| Export reserve (never spend) | 100 rows |
| Budget resets | 2026-11-01 |

The general rules from the first instructions still apply. Never export without
checking the row count first, log every export in `export_log`, do not invent data,
do not buy anything or change settings, and do not contact companies or apply to jobs.
In addition: on LinkedIn, Glassdoor or any other site, **only read**. Do not message
anyone, connect, follow, post, review or sign up for anything.

---

## 1. Why this round

- **Only 97 of 374 scored companies have a valuation.** Everyone else is scored as
  neutral on "room to grow" and "valuation step-up". Companies that were never checked
  by hand cannot climb, so the ranking favours the first top 40.
- **Time to cash is the main thing that separates good stages from bad ones.** An
  employee tender offer or secondary sale is a way to get cash before an IPO, so it is
  now an explicit check.

---

## 2. Part A – Profile checks (free: page visits, no exports)

Open each Crunchbase profile below and read its funding rounds table and recent news.
These are the companies ranked 18–80 by the analyst that you have not checked yet,
plus five whose valuation may be over $10B.

**Group 1 – might be over $10B (check first):**
Baseten, Reflection AI, Saronic, Ascend Elements, Sierra Space

**Group 2 – ranked 18–80, not yet checked (in rank order):**
Genius AI, Oligo Security, Proscia, Opentrons, Tractian, Sirona Medical,
Archy, Astronomer, Rightway, Cityblock Health, ICON, Impulse Space, Garner Health,
HappyRobot, ClickHouse, Ledgebrook, Horizon3.ai, Upstage, MarginEdge, Aven, Metaview,
Transcarent, Altruist, TRM Labs, Flyhomes, Cornelis Networks, Grow Therapy, LiveKit,
Firehawk Aerospace, Ashby, Oxide Computer Company, Gatik, Neros Technologies, Numeral,
Island, Vercel, Mainspring Energy, Group14 Technologies, EvenUp, Muon Space,
Tulip Interfaces, Claroty

If a profile is ambiguous (several companies with the same name), use the one whose
headquarters and description match the earlier company export.

For each company, add one row to a file called **`profile_checks.csv`**. Start the file
by copying all 40 rows of your existing `top_40` file (keep them unchanged, including the
fact-check notes), then append the new rows. Use exactly these columns:

| Column | What to write |
|---|---|
| `rank` | Leave blank for new rows |
| `company` | The Crunchbase organization name, **spelled exactly as in the company export** |
| `latest_valuation` | Latest post-money valuation. **Put the figure first**, formatted like `$1.4B` or `$650M`. Notes may follow it. Write `None disclosed` if there is none |
| `valuation_date` | Date, round type, and whether Crunchbase marks it Confirmed or Estimated, e.g. `2026-05-20 (Series D, Confirmed)` |
| `previous_valuation` | The previous **separately priced** round's post-money, same format (figure first), with round type and date. A tranche or extension of the same round does not count; write `NOT a separate prior round` and describe it |
| `red_flags` | Layoffs, down rounds, lawsuits, executive departures or regulatory trouble in the last 12 months. Write `None found` if there are none |
| `5x_check` | `5 × latest valuation`, then `plausible`, `stretch` or `no` |
| `why_it_could_be_very_large` | One sentence |

**Verification rule:** if Crunchbase marks a valuation as Estimated, search the web for
a reputable source (company announcement, TechCrunch, Bloomberg, Reuters, The
Information, WSJ, Axios). If none states the figure, append the word `UNVERIFIABLE`
in that cell, after the figure. The analyst's script treats any cell containing
`UNVERIFIABLE` as unknown, so use the word only for that purpose.

---

## 3. Part B – One funding-rounds export (up to 430 rows)

The goal is to get latest valuations for the many lower-ranked companies in one export,
instead of visiting hundreds of profiles.

Go to **Search → Funding Rounds** and apply:

| Filter | Value |
|---|---|
| Organization location | United States |
| Funding type | Series C, Series D, Series E, Series F |
| Announced date | 2024-11-01 to 2026-06-30 |
| Post-money valuation | Not blank |

Read the result count, then:

- **430 or fewer:** export it.
- **More than 430:** remove Series C and re-check. If it is still more than 430,
  **do not export now.** Record the counts in `export_log` and run the original search
  (with Series C) on or after **2026-11-01**, when the budget resets. Split it into date
  halves if needed, so that each export is 1,000 rows or fewer.

**Columns** must match the previous rounds export exactly:
Transaction Name, Transaction Name URL, Organization Location, Organization Name,
Organization Name URL, Funding Type, Money Raised, Money Raised Currency,
Money Raised (in USD), Announced Date, Post-Money Valuation, Post-Money Valuation
Currency, Post-Money Valuation (in USD), Lead Investors.

Name the file `funding-rounds-us-series-c-f-2024-11-to-2026-06.csv`.

---

## 4. Part C – Shortlist checks (free: page visits, no exports)

For each of the 15 companies below, research the questions using the company's
website, its careers page, LinkedIn company page (read only), Glassdoor or Blind (read
only), and news search. Record the answers in **`shortlist_checks.csv`**, one row per company.

**Shortlist:** Turing, Varda, Xona, Enveda, Serval, Hightouch, Eon, Whop, Profound,
Snorkel AI, Thyme Care, Fal, Owner, Reliable Robotics, Chaos

| Column | Question |
|---|---|
| `company` | Name as in the company export |
| `tender_offer` | Has the company run an employee tender offer or allowed employee secondary sales in the last 24 months? Give the date, size and price/valuation if reported, and the source link. `None found` if nothing |
| `ipo_signals` | Any public statement or credible report about IPO timing, an IPO-ready CFO hire, or a confidential filing in the last 12 months? Include a source link |
| `headcount_trend` | LinkedIn employee count now, and the 6- or 12-month growth % if LinkedIn shows it |
| `employee_sentiment` | Glassdoor overall rating and number of reviews, and the most common complaint in reviews from the last 12 months (one sentence). `No data` if none |
| `open_roles_for_user` | Number of open roles matching the target role in section 0, with one link to the most relevant one. `0` if none |
| `revenue_signal` | Most recent public revenue or ARR figure and date, with source. `None found` if none |
| `concerns` | Anything else that would worry a prospective employee (one or two sentences) |
| `sources` | Links to every source used, separated by spaces |

Do not guess. If a question cannot be answered from a reputable source, write `None found`.

---

## 5. What to hand back

Give the user these files, plus a short report:

1. `profile_checks.csv` (the old 40 rows plus about 47 new rows)
2. The funding-rounds export from Part B, or a note that it waits until 2026-11-01
3. `shortlist_checks.csv` (15 rows)
4. `export_log` with this round's entries

The report should list:
- Exports used this round and the export rows left this month
- Any company from Group 1 that is confirmed over $10B
- Any shortlist company with a tender offer in the last 24 months, which is the
  strongest early-cash signal
- Any company from Group 2 whose step-up was 3× or more (it may now rank highly)
- Every place you deviated from these instructions, and why

The user's analyst will then re-run the scoring with:

```bash
python3 research/score_all.py companies.csv old-rounds.csv,new-rounds.csv profile_checks.csv scored.csv
```
