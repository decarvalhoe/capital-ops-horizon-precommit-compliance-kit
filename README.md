# Kit pré-commit conformité dev — secrets, fichiers sensibles, licences, SBOM

Dépôt **template** prêt à cloner pour une PME sans chaîne de conformité. Outils libres uniquement :
[gitleaks](https://github.com/gitleaks/gitleaks) (MIT, secrets), [pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks)
(MIT, clés privées, gros fichiers), et deux scripts Python **sans dépendance** : liste des licences des paquets installés avec refus
configurable, et SBOM CycloneDX 1.5 minimal.

```sh
pipx install pre-commit          # ou : pip install pre-commit
pre-commit install
pre-commit run --all-files       # produit compliance/licenses.json et compliance/sbom.cdx.json
```

Adapter `--deny` dans `.pre-commit-config.yaml` (par défaut : GPL-3.0-only, AGPL-3.0-only — à décider selon votre politique).
Tests : `python3 -m unittest tests.test_scripts`.

Limites : SBOM et licences couvrent l'environnement Python courant (pas les dépendances npm/Go) ; l'exactitude des licences dépend des
métadonnées publiées par chaque paquet ; ce kit ne remplace pas une revue juridique. Licence MIT.
Test public gratuit de la ligue de paris Horizon (24.09.2026) : mesure = clones/vues GitHub uniquement, aucun traceur.
