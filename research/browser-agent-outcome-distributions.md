# Browser agent: published evidence on the shape of startup outcomes

Startup and venture outcomes are believed to follow a power law: most investments
return little and a few return enormous amounts. This round collects published numbers
on that shape, so the analysis can use tail probabilities instead of averages.

## Rules

1. **Read only.** Do not log in, sign up, enter an email address, fill in forms, or
   download anything behind a form. Record `gated` and move on.
2. **Never estimate.** Copy figures exactly, with the source URL and the exact sentence
   or table row (`quote`). If a figure is read from a chart without data labels, set
   `confidence` to `low` and note `read from chart`.
3. **Use DuckDuckGo or Bing for searches.** Google blocks automated searches.
4. **Paste results after every 10 rows** so nothing is lost if the browser crashes.

## What to find

Record every relevant figure as its own row:

`question, source, source_url, publication_date, period_covered, sample, metric, value, unit, breakdown, quote, confidence, notes`

| question | What to find | Where to look first |
|---|---|---|
| `vc_return_distribution` | Share of venture investments that return less than 1×, 1–3×, 3–5×, 5–10×, 10–50×, 50×+; and the share of total returns produced by the top 1%, 5% and 10% of deals | Correlation Ventures (published deal-outcome distribution), Horsley Bridge data as reported by Benedict Evans or Andreessen Horowitz, AngelList research on venture returns, Cambridge Associates |
| `tail_exponent` | Any estimated power-law exponent (alpha) for startup valuations, exit values or venture returns, with the method and sample | Academic papers and working papers (search "power law" with "venture capital returns" or "startup exits"), Kerr, Nanda and Rhodes-Kropf "Entrepreneurship as Experimentation" (2014) |
| `exit_value_distribution` | Distribution of acquisition prices and IPO valuations for venture-backed companies (e.g. share of exits under $50M, $50–100M, $100–500M, $500M–1B, $1B+) | PitchBook-NVCA Venture Monitor, Crunchbase News exit reports, Carta |
| `employee_outcomes` | Any published data on what employees actually received from startup equity, e.g. share of employees whose options ended up worth something, or payout distributions at exit | Carta, academic work on employee equity, compensation-data companies |
| `outcome_by_vintage` | Venture returns or exit rates by vintage year, especially 2015–2017 versus 2020–2021 | Cambridge Associates benchmarks, PitchBook, Carta |
| `founder_outcome_distribution` | Distribution of founder payouts at exit, including how often founders receive little or nothing at modest exits because investors are paid first | Carta founder reports, academic papers on liquidation preferences |

## Report back

- `published_distributions.csv`, pasted in full
- A short summary: which questions have solid numbers, which sources were gated, and
  any published tail exponents found (with sample and method)
