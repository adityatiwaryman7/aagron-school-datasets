# Aagron School AI dataset preparation

Status: proposed initial upload, 5 November 2026. No publishing has occurred as part of this preparation.

This repository is an audited catalog and a small, explicitly licensed starting dataset. It is not a complete school curriculum, an official board dataset, a production-ready training corpus, or sufficient evidence to train a general LLM from scratch.

## Included payload

`data/public/gsm8k/`: unchanged GSM8K train/test files from the available public-data archive, plus the upstream MIT license, README and source card. Preserve all upstream notices. Keep test data out of training. English arithmetic coverage does not establish CBSE, ICSE, state board, CA, MBA or competitive examination coverage.

## Repository layout

- `data/public/`: explicitly proposed public payload.
- `manifests/`: archive inventory, member hashes, JSONL syntax results, exact file overlaps, book-presence checks and dataset manifest.
- `sources/`: source register and previously recorded unavailable/protected references. License labels other than GSM8K remain archive declarations, not independently verified clearance.
- `docs/`: findings, rights decisions, missing-data list, storage and upload instructions.
- `scripts/verify.py`: verifies the exact proposed upload and checks JSONL syntax.
- `SHA256SUMS`: hashes of every repository file except itself and `UPLOAD_FILES.json`.
- `UPLOAD_FILES.json`: exact upload allowlist, sizes and hashes, including SHA256SUMS; excludes itself to avoid a circular hash.

The delivery bundle also contains `candidate_data_not_for_upload/` outside this repository. It holds six canonical synthetic SFT files. They are deliberately outside the upload scope. The full original archives are not copied into this delivery bundle; retain your originals and verify them against manifests/archives.json.

## Validation

Run `python3 scripts/verify.py` from this directory. For original archives, compare their SHA-256 and byte counts to `manifests/archives.json`. Archive CRC and SHA-256 checks detect corruption; they do not establish rights, data quality or model capability. Nested archives were hashed as files, not recursively audited. No generator or script from an input archive was executed.

No blanket dataset license is applied. GSM8K remains under its upstream MIT license. Other materials retain their owners' rights; source metadata does not grant reuse rights. Candidate synthetic content needs a chosen outbound license and provenance/content review before a separate publication decision.

See docs/FINDINGS.md and docs/UPLOAD_PLAN.md before publishing.
