# Pre-commit compliance kit — secrets, sensitive files, dependency licences, SBOM

[Version française](README.fr.md)

A **template repository** (click *Use this template* on GitHub, or clone it) for a small business without a compliance pipeline. Free tools only:
[gitleaks](https://github.com/gitleaks/gitleaks) (MIT, secrets), [pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks)
(MIT, private keys, large files, merge markers), and two Python scripts with **no dependency**: a list of installed package licences with a
configurable deny list, and a minimal CycloneDX 1.5 SBOM.

```sh
pipx install pre-commit          # or: pip install pre-commit
pre-commit install
pre-commit run --all-files       # writes compliance/licenses.json and compliance/sbom.cdx.json
```

Example output on a fresh virtual environment (synthetic, numbers vary):

```
gitleaks.................................................................Passed
detect private key.......................................................Passed
Python dependency licences (list + deny list)............................Passed
- 12 packages; 1 without a declared licence; 0 denied
Minimal CycloneDX SBOM (Python) from installed metadata..................Passed
- SBOM: 12 components -> compliance/sbom.cdx.json
```

Adjust `--deny` in `.pre-commit-config.yaml` (default: GPL-3.0-only, AGPL-3.0-only — decide according to your own policy).
Tests: `python3 -m unittest tests.test_scripts`.

## Feedback and support

Voluntary feedback goes through [GitHub Issues](https://github.com/decarvalhoe/capital-ops-horizon-precommit-compliance-kit/issues/new/choose)
(bug report or feedback form). Best effort, no guaranteed response time. See [SUPPORT.md](SUPPORT.md).

**Do not send private data.** Issues are public: never paste a real secret (even a revoked one), a real `licenses.json` or SBOM from a private
project, internal package names or hostnames. Reproduce with a synthetic example (a throwaway virtual environment with public packages).

## Limits

SBOM and licences cover the current Python environment (not npm/Go dependencies); licence accuracy depends on the metadata each package
publishes; this kit is neither a legal review nor a full validation of every third-party hook. MIT licence.
Free public test of the Horizon betting league (24 Sep 2026): measurement = GitHub clones/views only, no trackers.
