"""Convert funding rounds pulled through the Crunchbase MCP into the rounds-export format
that score_all.py reads.

Usage: python3 mcp_rounds_to_export.py MCP_ROUNDS.csv COMPANIES.csv OUT.csv

MCP_ROUNDS.csv columns: permalink, investment_type, announced_on, post_money_usd,
valuation_source (c100_confirmed / c200_estimated).
"""
import sys

import pandas as pd


def funding_type(investment_type):
    if investment_type == "series_unknown":
        return "Venture - Series Unknown"
    if investment_type.startswith("series_"):
        return "Series " + investment_type.split("_")[1].upper()
    return investment_type.replace("_", " ").title()  # seed, pre_seed, undisclosed, ...


def main(mcp_path, companies_path, out_path):
    r = pd.read_csv(mcp_path)
    c = pd.read_csv(companies_path)
    c["permalink"] = c["Organization Name URL"].str.rsplit("/", n=1).str[-1]
    names = c.set_index("permalink")["Organization Name"]
    out = pd.DataFrame({
        "Transaction Name URL": "mcp:" + r["permalink"] + ":" + r["investment_type"] + ":" + r["announced_on"],
        "Organization Name": r["permalink"].map(names),
        "Organization Name URL": "https://www.crunchbase.com/organization/" + r["permalink"],
        "Funding Type": r["investment_type"].map(funding_type),
        "Announced Date": r["announced_on"],
        "Post-Money Valuation (in USD)": r["post_money_usd"],
        "Valuation Source": r["valuation_source"],
    })
    unmatched = out["Organization Name"].isna().sum()
    out.dropna(subset=["Organization Name"]).to_csv(out_path, index=False)
    print(f"{len(out)} rounds, {out['Organization Name'].nunique()} companies, {unmatched} unmatched")


if __name__ == "__main__":
    main(*sys.argv[1:4])
