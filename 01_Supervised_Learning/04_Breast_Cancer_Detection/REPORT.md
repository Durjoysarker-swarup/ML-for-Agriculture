# Breast Cancer Detection — Detailed Report

## Executive Summary

This project applies Support Vector Machines (SVM) to classify breast tumors as malignant or benign. SVMs are particularly effective for binary classification in high-dimensional spaces. We explore kernel selection, hyperparameter tuning, and model evaluation for medical diagnosis tasks.

---

## Problem Statement

**Objective:** Classify breast tumors as malignant or benign from cellular measurements

**Dataset:** Wisconsin Breast Cancer Dataset
- 569 tumor samples
- 30 features extracted from cell nuclei images (radius, texture, perimeter, area, smoothness, etc.)
- Binary outcome: Malignant (212 cases) or Benign (357 cases)
- Imbalanced classes (~37% malignant, ~63% benign)

---

## Methodology

### 1. Data Exploration
- Feature distributions by cancer type
- Feature scaling requirements (critical for SVM)
- Class imbalance assessment
- Feature correlations

### 2. Data Preprocessing
- Feature standardization (Z-score normalization)
- Train-test split (80-20)
- Handling class imbalance through evaluation metrics

### 3. Compare different Model


## Key Findings

### A. Optimal SVM Configuration

**Best Performing Model:**
- **Kernel:** RBF (non-linear patterns in cancer features)
- **C:** 1.0 (balanced regularization)
- **Gamma:** 0.01 (wider influence per training point)

### B. Model Performance

**Accuracy:** 
1. Logistic Regression: 97
2. SVM: 95
3. Random Forest: 96


## Agricultural Connection

### How This Applies to Farming:

1. **Crop Disease Detection:**
   - Similar approach for identifying diseased plants from leaf characteristics
   - Size, texture, color of lesions → disease type
   - Non-linear patterns in disease progression

2. **SVM Applications in Agriculture:**
   - **Soil Classification:** Soil properties → crop suitability
   - **Pest Detection:** Image features → pest species identification
   - **Quality Grading:** Fruit characteristics → grade classification


---


---

## Skills Demonstrated

✅ Support Vector Machines fundamentals  
✅ Agricultural feature engineering concepts  

---

## References

- Dataset: UCI Machine Learning Repository — Breast Cancer Wisconsin
- SVM Reference: Vapnik, V. (1995) — Support Vector Networks
- Medical Imaging: Standard pathology feature extraction

---

**Last Updated:** June 2026
