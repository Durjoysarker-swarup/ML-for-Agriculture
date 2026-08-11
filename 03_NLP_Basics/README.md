# NLP Basics

Overview

This folder contains notebooks that introduce natural language processing techniques and examples for agricultural use cases: processing farmer notes, extracting structured information from reports, and simple text classification/topic modeling.

What's included
- Notebooks covering text cleaning, tokenization, TF-IDF, word embeddings (GloVe/Word2Vec), simple classifiers, and topic models (LDA).
- Utilities for dataset loading and sample preprocessing pipelines.

Prerequisites
- Python 3.8+ and dependencies from the root `requirements.txt`.
- If using pretrained embeddings, include download instructions or helper scripts in the notebook.

How to run
1. Install dependencies: `pip install -r requirements.txt`.
2. Place textual datasets into `data/`, or update the path at the top of the notebook.
3. Run the notebook sequentially; notebooks will typically include a `DATA_SCHEMA` block describing expected columns.

Best practices
- Normalize text (lowercasing, punctuation removal), but preserve domain-specific tokens (units, chemical names) when relevant.
- Use cross-validation or time-aware splits when modeling sequential reports.
- Evaluate with appropriate metrics for the task (F1 for imbalanced classification, coherence/perplexity for topics).

Privacy & ethics
- Scrub or anonymize any personally identifiable information (PII) in notes before sharing.

Contributing
- Add a short README cell to new notebooks describing the dataset, columns, and the research question being answered.