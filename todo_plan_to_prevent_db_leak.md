# Action Plan to Prevent Database Leakage on GitHub

## Immediate containment (today)
1. Make the repo private (if possible).
2. Remove sensitive files from the current tree:
   - pg_backup_2026_02_09.sql
   - removed_ads.csv
   - listed_ads.csv
   - any other DB dumps or raw data exports
3. Add a .gitignore rule to prevent future dumps from being committed.

## Purge history (critical)
1. Use git filter-repo (preferred) or BFG to delete the dump files from all commits.
2. Force-push rewritten history to GitHub.
3. Instruct collaborators to re-clone.

## Rotate and audit
1. Rotate any credentials or tokens that might be in the dumps or configs.
2. Audit the repo for any secrets (API keys, passwords).

## Safer data handling going forward
1. Keep real dumps out of git entirely.
2. If you need sample data, use anonymized or synthetic data.
3. Store large or sensitive datasets in:
   - private object storage
   - private artifacts
   - or a secured data registry
4. Add a pre-commit hook that blocks .sql, .csv, .dump unless explicitly allowed.

## Optional hardening
1. Enable GitHub secret scanning and push protection.
2. Add a CI check that fails on large or forbidden file patterns.
