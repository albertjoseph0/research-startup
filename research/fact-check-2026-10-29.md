# Fact check of the cohort study and shortlist (2026-10-29)

Adversarial web research against the claims in `stage-cohort-study.md` and the hand-checked
top 40. Corrections were applied by re-running `rescore_top40.py` on a corrected copy of the
top-40 input.

## Analysis claims

| Claim | Verdict | Evidence |
|---|---|---|
| Facebook employee #100 joined far below the final value | Holds | Accel round valued Facebook at ~$87.5–100M (2005); ~$500M by April 2006 ([Fortune](https://fortune.com/2011/01/11/timeline-where-facebook-got-its-funding)) |
| Dropbox at ~100 people was already worth billions | Holds | ~$4B valuation in 2011 with ~87–90 employees ([HBR via tagteam](https://tagteam.harvard.edu/hub_feeds/4673/feed_items/16419695), [Gigaom](https://om.co/gigaom/how-big-is-dropbox-hint-very-big/)) |
| Most early-stage companies take a long time to exit | Holds | Median tech IPO age ~12 years in 2025 ([Ritter data](https://site.warrington.ufl.edu/ritter/files/IPOs-Age.pdf)) |
| D/E advantage may be 2020–21 bubble timing | Supported | 2021 IPO value ~$1T, ~2× 2020; ~half of 2021 $1B+ listings later fell below $500M ([Crunchbase News](https://news.crunchbase.com/public/2021-ipo-companies-went-public-valuation-analysis-2023)) |
| Crunchbase under-reports closures | Supported | Crunchbase has said it does not track closures well ([Crunchbase blog](https://about.crunchbase.com/blog/mining-the-series-a-crunch)) |
| "Time to cash" = time to IPO or acquisition | **Incomplete** | Tender offers are at a four-year high and mostly priced at or above the last round ([Carta](https://carta.com/data/tender-offer-update-h1-2026/)); ~60% are run by companies valued $1–10B ([Freestone](https://www.freestonecapital.com/insights/what-is-a-private-company-tender-offer-a-guide-for-employees/)). Employees at late-stage private companies can get partial liquidity without an exit, which the study did not count. |
| Paper multiples equal employee multiples | **Overstated** | Common stock/409A is typically well below the preferred price, and preferences rank ahead of common ([Carta](https://carta.com/uk/en/learn/equity/common-stock-vs-preferred-stock/)) |
| Crunchbase "Estimated" valuations are data | **Weak** | They are model-generated at the round date when no confirmed figure exists ([Crunchbase support](https://support.crunchbase.com/hc/en-us/articles/50305596457747-Crunchbase-Post-Money-Valuation-Data)) |

## Shortlist corrections

| Company | Finding | Effect |
|---|---|---|
| Fal | Raised at ~$8B in spring 2026; in talks at $15–20B ([The Information via X](https://x.com/theinformation/status/2104632290743615999), [Sovereign](https://www.sovereignmagazine.com/article/fal-fireworks-inference-valuations-15b-30b)) | Excluded |
| Varda | $1.6B Series D announced 2026-09-30, not February ([Reuters via WHBL](https://whbl.com/2026/09/30/varda-raises-250-million-at-1-6-billion-valuation-to-scale-orbital-drug-manufacturing/)); prior valuation reported anywhere from $500M to $1.2B ([multiples.vc](https://multiples.vc/private-comps/varda)) | Valuation growth set to unknown; #1 → #3 |
| Vouch | 2025 Series D size and valuation undisclosed; $1.3B was a Crunchbase estimate ([The Digital Banker](https://thedigitalbanker.com/vouch-expands-insurance-capabilities-with-startsure-acquisition-and-announces-series-d-financing-led-by-allegis-capital/), [Caplight](https://www.caplight.com/company/vouch-inc)) | Valuation unknown, small penalty; #4 → #23 |
| Medallion | No disclosed valuation; ~$440M estimate; secondary quote implies ~$114M ([StockAnalysis](https://stockanalysis.com/private/medallion/)) | Penalised; #10 → #33 |
| Lumilens | $5.5B confirmed ([TechFundingNews](https://techfundingnews.com/lumilens-debuts-with-700m-war-chest-and-5-5b-valuation-after-emerging-from-stealth/)); prior Series B valuation unverified | Valuation growth unknown; #12 → #17 |
| Celero | $3B+ confirmed ([pulse2](https://pulse2.com/celero-communications-raises-275-million-series-c-at-more-than-3-billion-valuation/)); prior valuation not disclosed; chip not yet shipping at volume ([FourWeekMBA](https://fourweekmba.com/ai-celero-275m-series-c-coherent-optics-ai-infrastructure/)) | Valuation growth unknown; #15 → #22 |

Confirmed as recorded: Xona $2.45B ([SatNews](https://satnews.com/2026/10/22/xona-space-systems-secures-250m-series-d-at-2-45b-valuation-to-scale-pulsar-pnt-fleet/)),
Profound $1.8B from $1B ([CMSWire](https://www.cmswire.com/digital-experience/profound-nabs-180m-to-scale-ai-marketing-platform/)),
Serval $3B from $1B, announced today ([Reuters via WBOW](https://1027wbow.com/2026/10/29/serval-triples-valuation-to-3-billion-as-businesses-adopt-ai-workflow-automation/)),
Hightouch $2.75B from $1.2B ([Dealroom](https://dealroom.co/news/128216-hightouch-raises-150m-at-2-75b-to-make-ai-agents-the-future-of-marketing/)),
Whop $5.1B from $1.6B ([TNW](https://thenextweb.com/news/whop-200m-series-d-5-1b-valuation-sequoia)),
Chaos $4.5B from $2B ([Ensemble VC](https://www.ensemble.vc/research/chaos-notches-4-5b-valuation-in-510m-series-d)),
Thyme Care $2B+, profitable per one source ([MedCity News](https://medcitynews.com/2026/09/thyme-care-raises-125m-launches-new-oncology-parent-entity/)),
Enveda $2B, early clinical data only ([Pulse 2.0](https://pulse2.com/enveda-raises-311-million-series-e-led-by-catalio-capital-management-bringing-total-funding-to-over-845-million/amp/)),
Eon $4B from $1.4B ([SDxCentral](https://www.sdxcentral.com/news/data-backup-startup-eon-soars-to-4b-valuation-after-300m-investment/)),
Snorkel AI $3.5B, 13% layoff predates the round ([TechCrunch](https://techcrunch.com/2026/09/22/snorkel-ai-triples-valuation-to-3-5b-as-demand-for-ai-training-data-booms)).
