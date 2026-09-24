#!/usr/bin/env python3
"""Lists the licences of installed Python packages (importlib metadata) and fails if a denied licence is present.
No external dependency. Usage: dependency_licenses.py [--deny "SPDX1,SPDX2"] [--out file.json]"""
import argparse, json, os, sys
from importlib import metadata

def licence_of(dist):
    m = dist.metadata
    lic = (m.get("License-Expression") or "").strip()
    if not lic:
        lic = (m.get("License") or "").strip()
    if not lic or lic.upper() == "UNKNOWN" or len(lic) > 80:
        for c in m.get_all("Classifier") or []:
            if c.startswith("License ::"):
                lic = c.split("::")[-1].strip(); break
    return lic or "UNKNOWN"

def main():
    p = argparse.ArgumentParser(); p.add_argument("--deny", default=""); p.add_argument("--out", default="")
    a = p.parse_args()
    deny = [d.strip().lower() for d in a.deny.split(",") if d.strip()]
    rows = sorted(({"name": d.metadata["Name"], "version": d.version, "license": licence_of(d)} for d in metadata.distributions()), key=lambda r: r["name"].lower())
    bad = [r for r in rows if any(x in r["license"].lower() for x in deny)]
    if a.out:
        os.makedirs(os.path.dirname(a.out) or ".", exist_ok=True)
        with open(a.out, "w") as f: json.dump({"packages": rows, "denied": bad}, f, indent=2)
    print(f"{len(rows)} packages; {sum(1 for r in rows if r['license']=='UNKNOWN')} without a declared licence; {len(bad)} denied")
    for r in bad: print(f"  DENIED {r['name']} {r['version']}: {r['license']}")
    sys.exit(1 if bad else 0)

if __name__ == "__main__":
    main()
