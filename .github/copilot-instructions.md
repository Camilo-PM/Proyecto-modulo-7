<!-- .github/copilot-instructions.md -->
### Purpose
This file gives concise, actionable guidance to AI coding agents working in this repository so they can be productive immediately.

Guiding assumptions
- This repo is a small data-analysis project (Jupyter notebooks + dataset).
- Primary workspace root: `Proyecto-modulo-7/` (use the nested folder that contains `Notebooks/` and `vehicles_us.csv`).

Quick architecture (big picture)
- Data: `vehicles_us.csv` at the repository root — single CSV source used by the notebooks.
- Analysis: interactive work lives in `Notebooks/EDA.ipynb`. There are no dedicated `src/` modules yet.
- Environment: a local virtual environment is used (`.venv/`); dependencies are listed in `requirements.txt` (currently empty).

Developer workflows (explicit)
- Activate the venv (PowerShell):
  - `& "${PWD}\.venv\Scripts\Activate.ps1"`
- Install dependencies: `pip install -r requirements.txt` (add pinned deps to `requirements.txt` before installing in CI or new clones).
- Run notebooks: start Jupyter and open `Notebooks/EDA.ipynb`:
  - `jupyter lab` or `jupyter notebook`
- Data edits: update `vehicles_us.csv` in place. If the dataset grows very large, propose adding a `data/` folder and documenting ingestion steps.

Repository conventions and patterns
- Notebooks are the primary artifact for analysis. When converting analysis to reusable code, create a `src/` package at repo root and add tests there.
- Keep notebooks runnable: prefer reproducible cell order and include a single setup cell that documents imports and data paths.
- `requirements.txt` should be populated with pinned package versions (e.g., `pandas==1.5.3`) before sharing or CI runs.

AI agent-specific instructions
- When changing notebooks, preserve cell outputs only if explicitly asked; otherwise clear outputs and focus on code/content changes.
- Prefer small, focused commits: 1 feature/bug per commit and mention changed files (e.g., `Notebooks/EDA.ipynb`, `requirements.txt`).
- If adding scripts, also add a small `README.md` or update the top-level `README.md` to explain how to run them.
- If asked to run or validate code, describe the exact commands you expect the user to run locally (we cannot run the user's environment from the repo directly).

Integration points / external dependencies
- No external services or CI configs were found in the repository. If you plan to add CI, use GitHub Actions and ensure the workflow activates `.venv` or uses a clean Python environment and installs `requirements.txt`.

Files to inspect for context
- `Notebooks/EDA.ipynb` — primary analysis notebook.
- `vehicles_us.csv` — dataset used by the notebook.
- `requirements.txt` — dependencies (currently empty; update with pinned versions).
- `.venv/` — local virtual environment seen in local terminal usage; do not commit virtual environments to the repo.

If something isn't discoverable
- Ask the user to confirm the repository root (there are duplicated top-level folders in the workspace). Point to the nested `Proyecto-modulo-7/` that contains `Notebooks/` as the canonical repo root.

Questions for maintainers (when unresolved)
- Do you want notebook outputs committed or cleared on change?
- Should I add a `src/` layout and a simple test harness if requested?

If this file already existed, merge policy
- Preserve any existing human-written sections. Insert or update the sections above, and avoid overwriting maintainers' notes.

End of file — please tell me which parts need more detail or examples.
