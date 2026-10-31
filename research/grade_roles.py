"""Grade a browser-agent role_requirements.csv against Albert's profile and summarise per company.

Profile: backend/platform/infra/systems/devtools/data SWE, Python and C++, mid-level (senior is a stretch), US.
Grades use only the structured fields (years, level, location, languages, clearance), not the agent's prose.
"""
import re
import sys

import pandas as pd

# Usage: python3 grade_roles.py ROLE_REQUIREMENTS.csv OUT_DIR
roles_path, out_dir = sys.argv[1], sys.argv[2]
r = pd.read_csv(roles_path)

years = pd.to_numeric(r.years_required.str.extract(r"(\d+)")[0], errors="coerce")
level = r.level.fillna("").str.lower()
any_level = level.str.contains("all levels|early career|mid")
above = level.str.contains("staff|principal|lead|manager|founding") & ~any_level
senior = level.str.contains("senior|sr\\.|experienced") & ~any_level

text = (r.must_have_skills.fillna("") + " " + r.role_title.fillna("") + " " + r.work_arrangement.fillna(""))
blockers = pd.Series("", index=r.index)
for label, pat in [("non-US location", r"Brazil or Colombia|^hybrid \(Cracow"),
                   ("Hebrew required", r"Hebrew"),
                   ("manager experience required", r"as an engineering manager|people management|Engineering Manager")]:
    hit = text.str.contains(pat, case=False, regex=True)
    blockers = blockers.where(~hit, blockers + label + "; ")
blockers = blockers.str.rstrip("; ")

r["years_min"] = years
r["grade"] = "reachable"
r.loc[senior | years.between(5, 6), "grade"] = "stretch"
r.loc[above | (years >= 7), "grade"] = "out of range"
r.loc[blockers != "", "grade"] = "blocked"
r["blockers"] = blockers
r["us_person_required"] = r.citizenship_or_clearance.str.contains("ITAR|U\\.S\\. person|US-person|clearance",
                                                                 case=False, na=False)
langs = r.languages.fillna("") + " " + r.must_have_skills.fillna("")
r["python_or_cpp"] = langs.str.contains(r"\bPython\b|C\+\+|\bC\b", regex=True)
r["remote_us"] = r.work_arrangement.str.contains(r"remote", case=False, na=False)


def base_k(s):
    """Return (low, high) base pay in $K from strings like '$180K – $250K' or 'USD 176200 - 281900'."""
    if not isinstance(s, str):
        return (None, None)
    vals = []
    for num, k in re.findall(r"\$?\s?(\d[\d,]*(?:\.\d+)?)\s*([kK])?", s):
        v = float(num.replace(",", ""))
        v = v if k else v / 1000
        if 50 <= v <= 1000:
            vals.append(v)
    return (min(vals), max(vals)) if len(vals) >= 2 else (None, None)


pay = r.salary_range.map(base_k)
r["base_low_k"] = pay.str[0]
r["base_high_k"] = pay.str[1]

order = {"reachable": 0, "stretch": 1, "out of range": 2, "blocked": 3}
r["_o"] = r.grade.map(order)
r = r.sort_values(["tier", "_o", "python_or_cpp", "company"], ascending=[True, True, False, True])
cols = ["tier", "company", "grade", "role_title", "level", "years_required", "languages", "python_or_cpp",
        "work_arrangement", "remote_us", "us_person_required", "blockers", "salary_range", "base_low_k",
        "base_high_k", "visa_sponsorship", "interview_process", "must_have_skills", "nice_to_have", "fit_notes",
        "role_url"]
r[cols].to_csv(f"{out_dir}/role_shortlist_r10.csv", index=False)

ok = r[r.grade.isin(["reachable", "stretch"])]


def summary(g):
    k = ok[ok.company == g.name]
    best = k.sort_values(["_o", "python_or_cpp"], ascending=[True, False]).role_title.head(3)
    visa = g.visa_sponsorship[g.visa_sponsorship != "not stated"]
    return pd.Series({
        "roles_checked": len(g),
        "roles_reachable": int((g.grade == "reachable").sum()),
        "roles_stretch": int((g.grade == "stretch").sum()),
        "roles_ok_python_cpp": int(k.python_or_cpp.sum()),
        "roles_ok_remote": int(k.remote_us.sum()),
        "roles_us_person_only": int(g.us_person_required.sum()),
        "base_pay_k_ok_roles": (f"{k.base_low_k.min():.0f}-{k.base_high_k.max():.0f}"
                                if k.base_low_k.notna().any() else ""),
        "best_roles": "; ".join(best),
        "visa_sponsorship": visa.iloc[0] if len(visa) else "not stated",
    })


per = r.groupby("company").apply(summary, include_groups=False)
per.to_csv(f"{out_dir}/role_summary_r10.csv")
print(r.grade.value_counts().to_string())
print(per.sort_values("roles_reachable", ascending=False).to_string())
