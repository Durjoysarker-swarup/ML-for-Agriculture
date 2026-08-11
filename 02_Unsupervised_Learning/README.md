# Unsupervised Learning

Overview

This directory introduces unsupervised learning techniques and exploratory data analysis workflows that are useful for agricultural data (e.g., clustering field sensor patterns, dimensionality reduction for remote sensing, and anomaly detection in equipment logs).

What's included
- Notebooks demonstrating clustering (K-Means, hierarchical, DBSCAN), dimensionality reduction (PCA, t-SNE, UMAP), and anomaly detection methods.
- Visualizations to help interpret cluster structure and latent representations.

Prerequisites
- Python 3.8+ and dependencies in `requirements.txt`.
- Small example datasets are recommended; for large satellite datasets provide scripts to download or create sample subsets.

How to run
1. Install dependencies: `pip install -r requirements.txt`.
2. Launch Jupyter Lab and open notebooks in this folder.
3. Ensure dataset paths are pointed to a `data/` directory or change the `DATA_DIR` variable in the notebook.

Best practices
- Always scale or normalize features before running clustering or distance-based methods.
- Use silhouette scores, Davies–Bouldin index, or visual inspection of embeddings to choose cluster counts.
- For visualization, reduce to 2D/3D embeddings and color by known labels when available to validate unsupervised results.

Contributing
- Describe the dataset schema and any pre-processing done to generate example artifacts.
- Include brief inline comments explaining parameter choices (e.g., `eps` for DBSCAN) and recommended diagnostics.

Notes for deployment
- Unsupervised models are often used as preprocessing or monitoring tools — document how outputs (cluster labels, anomaly scores) should be consumed by downstream systems.