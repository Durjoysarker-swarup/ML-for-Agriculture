# Supervised Learning

Overview

This directory contains Jupyter notebooks and supporting resources that teach and demonstrate supervised learning techniques applied to agricultural problems such as crop classification, yield prediction, and disease detection.

What's included
- Notebooks named with a numeric prefix and a short descriptive title (e.g., `01_classification_simple.ipynb`).
- Example datasets or dataset loaders (not always included; see each notebook header).
- Utility notebooks for preprocessing, feature engineering, and model evaluation.

Prerequisites
- Python 3.8+ recommended
- Install dependencies: `pip install -r requirements.txt` from repository root
- Optional: GPU for larger models (see individual notebooks)

How to run
1. Clone the repository and install dependencies.
2. Start Jupyter Lab: `jupyter lab` or `jupyter notebook`.
3. Open a notebook and run cells sequentially. If a notebook expects a `data/` directory, create one at the repository root and add the dataset there, or update the `DATA_DIR` variable at the top of the notebook.

Notebook conventions
- Each notebook should start with a short description, learning objectives, and a `Requirements` cell that lists any datasets and the column schema expected.
- Include a `RANDOM_SEED` constant near the top to ensure reproducibility when comparing models.
- For results that take a long time, include a short summary cell with final metrics and a link to the training cell(s).

Reproducibility & evaluation
- Use train/validation/test splits and report metrics appropriate for the task (accuracy, precision/recall/F1 for classification; RMSE/MAE for regression).
- Include baseline models (e.g., linear/logistic regression) for comparison before using complex algorithms.

Contributing
- When adding new notebooks, provide a brief README cell in the notebook describing data source, expected input format, and required compute resources.
- Keep long-running model training behind clear flags or use saved model artifacts to reproduce results quickly.

Resources & references
- Link to any external datasets, papers, or libraries used at the top of each notebook.