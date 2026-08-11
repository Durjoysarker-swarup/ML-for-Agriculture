# Contributing to ML-for-Agriculture

Thank you for contributing! Contributions that improve reproducibility, clarity, and real-world application are especially welcome.

What to contribute
- New notebooks with clear learning objectives and dataset documentation.
- Small, reproducible sample datasets or download scripts for larger datasets.
- Fixes to documentation, README improvements, and reproducibility fixes.
- Code to automate evaluation or create reproducible artifacts (e.g., scripts to export final predictions and metrics).

Notebook checklist (please follow)
- Title and authors with date.
- Learning objectives (3–5 bullets).
- Data section describing source, file names, and schema.
- Requirements cell listing packages beyond repository `requirements.txt` (if any).
- Explicit random seed: `RANDOM_SEED = 42` (or similar) for reproducibility.
- Final summary cell with results, metrics, and short interpretation.
- If notebook is long-running, provide a small sample dataset and a `SAMPLE_MODE` or flag to run a quick demo.

How to submit
1. Fork the repository and create a branch: `git checkout -b feat/my-notebook`
2. Add your notebook(s) and any helper scripts to an appropriate folder.
3. Run `tools/check_readmes.py` to ensure your folder has a README.md and metadata.
4. Commit and push, then open a pull request with a clear description and expected runtime.

Reviewer expectations for PRs
- Include the PR checklist: reproducibility steps, example commands, and expected outputs.
- If adding datasets, prefer adding small samples or providing a download script instead of adding large files to the repo.

Code style
- Keep notebook cells focused and well-commented.
- For Python scripts, follow common conventions (PEP8) and include docstrings.

Security & privacy
- Do not include PII or sensitive credentials.
- For datasets with privacy concerns, provide anonymized samples and detailed instructions for obtaining access.

License and ownership
- By contributing you agree to license your contribution under the repository's MIT license.

Thank you for helping improve ML-for-Agriculture!