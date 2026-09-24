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

First run: pre-commit downloads the pinned hooks (and a Go toolchain for gitleaks if none is installed; about 20 s and ~50 MB here, network required).
Output observed on 2026-09-24 in a throwaway environment (rehearsal receipt in the Horizon repo):

```
Detect hardcoded secrets......................................................Passed
detect private key............................................................Passed
check for added large files...................................................Passed
check for merge conflicts.....................................................Passed
Python dependency licences (list + deny list).................................Passed
Minimal CycloneDX SBOM (Python) from installed metadata.......................Passed
```

Rehearsed refusals (synthetic defects): fake AWS key, GitHub token and private key (gitleaks, `private-key`), the same key file (`detect private key`),
a 1.5 MB binary (`check for added large files`), leftover `<<<<<<<` markers (`check for merge conflicts`, needs `--assume-in-merge`, set in the config),
a package declaring `GPL-3.0-only` (licence hook exits 1). A real `git commit` is blocked when a hook fails.

Notes: the two local hooks scan the Python environment that `python3` resolves to on your PATH (activate the virtual environment you want
audited before committing). A package with no declared licence is listed as `UNKNOWN` and does **not** fail the hook: review those by hand.
The SBOM validated with 0 errors against the official CycloneDX 1.5 JSON schema (`bom-1.5.schema.json`, 2026-09-24).

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
