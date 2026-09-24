# Kit pré-commit conformité dev — secrets, fichiers sensibles, licences, SBOM

[English version](README.md)

Dépôt **template** (bouton *Use this template* sur GitHub, ou clonage) pour une PME sans chaîne de conformité. Outils libres uniquement :
[gitleaks](https://github.com/gitleaks/gitleaks) (MIT, secrets), [pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks)
(MIT, clés privées, gros fichiers), et deux scripts Python **sans dépendance** : liste des licences des paquets installés avec refus
configurable, et SBOM CycloneDX 1.5 minimal. Sorties des scripts en anglais.

```sh
pipx install pre-commit          # ou : pip install pre-commit
pre-commit install
pre-commit run --all-files       # produit compliance/licenses.json et compliance/sbom.cdx.json
```

Adapter `--deny` dans `.pre-commit-config.yaml` (par défaut : GPL-3.0-only, AGPL-3.0-only — à décider selon votre politique).
Tests : `python3 -m unittest tests.test_scripts`.

## Retours et support

Retour volontaire via [GitHub Issues](https://github.com/decarvalhoe/capital-ops-horizon-precommit-compliance-kit/issues/new/choose). Meilleur effort, sans délai garanti. Voir [SUPPORT.md](SUPPORT.md).

**Ne transmettez aucune donnée privée.** Les issues sont publiques : jamais de secret réel (même révoqué), de `licenses.json` ou de SBOM d'un projet privé, de noms de paquets ou d'hôtes internes. Reproduisez avec un exemple synthétique (environnement virtuel jetable, paquets publics).

## Limites

SBOM et licences couvrent l'environnement Python courant (pas les dépendances npm/Go) ; l'exactitude des licences dépend des
métadonnées publiées par chaque paquet ; ce kit ne constitue ni revue juridique ni validation intégrale de tous les hooks tiers. Licence MIT.
Test public gratuit de la ligue de paris Horizon (24.09.2026) : mesure = clones/vues GitHub uniquement, aucun traceur.
