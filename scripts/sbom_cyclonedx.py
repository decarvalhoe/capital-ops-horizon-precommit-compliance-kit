#!/usr/bin/env python3
"""Minimal CycloneDX 1.5 SBOM (JSON) of installed Python packages, no external dependency.
Usage: sbom_cyclonedx.py [--out compliance/sbom.cdx.json]"""
import argparse, datetime, json, os, uuid
from importlib import metadata

def main():
    p = argparse.ArgumentParser(); p.add_argument("--out", default="compliance/sbom.cdx.json"); a = p.parse_args()
    comps = []
    for d in sorted(metadata.distributions(), key=lambda d: d.metadata["Name"].lower()):
        name, ver = d.metadata["Name"], d.version
        comps.append({"type": "library", "name": name, "version": ver, "purl": f"pkg:pypi/{name.lower()}@{ver}",
                      "bom-ref": f"pkg:pypi/{name.lower()}@{ver}"})
    bom = {"bomFormat": "CycloneDX", "specVersion": "1.5", "serialNumber": f"urn:uuid:{uuid.uuid4()}", "version": 1,
           "metadata": {"timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(), "tools": [{"name": "sbom_cyclonedx.py (pre-commit compliance kit)"}]},
           "components": comps}
    os.makedirs(os.path.dirname(a.out) or ".", exist_ok=True)
    with open(a.out, "w") as f: json.dump(bom, f, indent=2)
    print(f"SBOM: {len(comps)} components -> {a.out}")

if __name__ == "__main__":
    main()
