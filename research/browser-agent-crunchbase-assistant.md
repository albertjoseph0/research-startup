# Browser agent: get as much as possible from the Crunchbase homepage assistant

The Crunchbase homepage has an AI chat box ("Ask me about Crunchbase data"). Using it does
not seem to use up any of the user's data allowance, so we want to find out what it can
answer and collect every useful answer. It already failed one complex question. It is
probably better at simple questions and at listing companies than at calculations.

Work through the levels in order. Every answer gets recorded, including failures.

---

## Rules

1. **Only use the homepage assistant** at crunchbase.com. Do not export anything.
   Do not page through Advanced Search result tables. If the assistant offers a search
   link, record the URL but do not open it to copy rows.
2. **Ask one question at a time, at a normal pace.** If the assistant shows a usage
   limit, rate-limit or error message, stop and report it word for word.
3. **Start a new chat for each level** (refresh the homepage), so earlier answers
   don't affect later ones.
4. **Ask each question exactly as written first.** If the answer is "couldn't find",
   empty, or clearly misunderstands the question, try the rephrasings given (up to 2).
   Record every attempt.
5. **Copy answers word for word.** Copy every table in full, every number unrounded,
   and any note about how it was calculated. If the assistant shows a "show more",
   "view all" or similar control inside the chat, use it and copy everything shown.
6. **Do not judge or fix answers.** Fill in `matches_expected` only where an expected
   answer is given: `yes` if within 10%, `no` otherwise, `n/a` if none is given.

---

## Output

Paste two things into your reply:

**A. `assistant_log.csv`**, one row per attempt:
`level,question_id,attempt,question_text,answer_text,expected,matches_expected,search_url,notes`

**B. Every table or list the assistant returned**, each as its own CSV block headed
with its `question_id`. Keep all columns it gave.

Send results after each level, so nothing is lost if the browser crashes.

---

## Level 0 – What can it do? (no expected answers)

- **0a.** What kinds of questions can you answer? Can you count companies, calculate medians or averages, and group results?
- **0b.** Can you list companies matching filters, and how many results can you show at once?
- **0c.** Do you have access to funding round post-money valuations, acquisition prices and IPO valuations?

## Level 1 – Single company lookups (checks its facts)

| id | Question | Expected |
|---|---|---|
| 1a | What is LiveKit's latest funding round, its date, and its post-money valuation? | Series C, Jan 2026, $1B |
| 1b | What was Hightouch's post-money valuation at its Series D in April 2026? | $2.75B |
| 1c | Has ClickHouse raised at a valuation above $10 billion? Give the round and date. | Yes, $15B Series D, Jan 2026 |
| 1d | Was MaintainX acquired? By whom and for how much? | Autodesk, $3.575B, May 2026 |

## Level 2 – Simple counts (checks whether it can count at all)

| id | Question | Expected |
|---|---|---|
| 2a | How many companies headquartered in the United States announced a Series B funding round between 2016-01-01 and 2018-12-31? | about 2,170 |
| 2b | How many companies in total have more than 10,000 employees? | about 25,300 |
| 2c | How many private, active, for-profit companies headquartered in the United States have a last funding type of Series C, D, E or F, a last funding date on or after 2024-11-01, and 101 to 5,000 employees? | about 406 |
| 2d | How many companies have a last funding type of Series J? | 1 |

Rephrasings if a count fails: drop one filter at a time (start with the date), or ask
"Show me…" instead of "How many…".

## Level 3 – Medians (checks calculations)

| id | Question | Expected |
|---|---|---|
| 3a | What is the median post-money valuation of Series D funding rounds announced by United States companies between 2026-07-01 and 2026-10-29? | about $1.15B |
| 3b | What is the median post-money valuation of Series B funding rounds announced by United States companies between 2026-07-01 and 2026-10-29? | about $353M |
| 3c | What was the median post-money valuation of Series D funding rounds announced by United States companies between 2015-01-01 and 2019-12-31? | about $327M |

## Level 4 – Outcomes for groups of companies (the real question, broken into small pieces)

These are the pieces of the main research question: when people joined companies at different
valuations, how often did the company later go public or get acquired? Ask each cell
separately. The first two have known answers.

| id | Question | Expected |
|---|---|---|
| 4a | Of United States companies that raised a Series C round between 2016-01-01 and 2018-12-31, what percentage have since been acquired? | about 43% |
| 4b | Of United States companies that raised a Series C round between 2016-01-01 and 2018-12-31, what percentage have since gone public through an IPO? | about 18% |

Then, for each **valuation band** and **stage** below (8 combinations), ask these three
questions. Use the ids `4-<band>-<stage>-1/2/3`, e.g. `4-300M1B-late-2`.

Bands: `100M300M` = $100M to $300M · `300M1B` = $300M to $1B · `1B3B` = $1B to $3B · `3B10B` = $3B to $10B

Stages: `early` = Series A or Series B · `late` = Series C, Series D or Series E

1. How many United States companies raised a [stage rounds] round between 2015-01-01 and 2019-12-31 at a post-money valuation between [band]?
2. Of those companies, how many later went public or were acquired?
3. Of those companies, how many went public or were acquired within 4 years of that round, at an IPO valuation or acquisition price at least 5 times that round's post-money valuation?

## Level 5 – Lists (we can calculate ourselves if it can list)

If counts and medians failed but it can list companies, these lists let the analyst
calculate the answers directly. Ask for as many rows as it will show. If it caps the
list, split by year (ask once per year from 2015 to 2019) and by band.

- **5a.** List United States companies that raised a Series C, D or E round between 2015-01-01 and 2019-12-31 at a post-money valuation between $300M and $1B. For each, give the company name, round type, round date, post-money valuation, current status (private, acquired, public or closed), and exit date and exit value if it exited.
- **5b.** Same as 5a for $1B to $3B.
- **5c.** Same as 5a for Series A or B rounds between $300M and $1B.

## Level 6 – Series B companies today (fills the biggest gap in the current list)

- **6a.** List United States companies whose most recent funding round is a Series B announced on or after 2025-01-01, with a post-money valuation between $300M and $1.5B. For each, give the name, round date, amount raised, post-money valuation, number of employees, and Crunchbase URL if available.
- **6b.** Same as 6a, but for companies whose most recent round is a Series C announced on or after 2025-01-01 and whose valuation is between $300M and $1.5B.

If a list is capped, split it by quarter of the round date and repeat.

## Level 7 – Is the wait for cash getting longer? (optional)

- **7a.** Of United States companies that raised a Series C round in 2015 or 2016, what percentage went public or were acquired within 4 years of that round?
- **7b.** Same for Series C rounds in 2018 or 2019.

---

## Report back

After all levels, finish with a short summary:
- Which levels worked (answers present and matching expected values) and which failed
- Any usage limit or error messages, word for word
- How many rows each list returned, and whether lists were capped (and at what number)
