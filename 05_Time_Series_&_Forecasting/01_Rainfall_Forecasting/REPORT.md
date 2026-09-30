# Rainfall Forecasting — Detailed Report

## Executive Summary

This project builds a next-day rain prediction model from daily weather observations. Using logistic regression with SMOTE to handle class imbalance, the model predicts whether it will rain tomorrow (`RainTomorrow`). It reaches ~79% accuracy and an ROC-AUC of ~0.86, with strong recall on rainy days.

---

## Problem Statement

**Objective:** Predict whether it will rain tomorrow from today's weather measurements

**Practical Impact:** Early rain forecasts support planning in agriculture, transport, events, and water management

**Dataset:** `weather.csv`, ~142,000 daily records with 23 original columns, including:
- Date and location
- Temperature (min, max, 9am, 3pm)
- Rainfall, evaporation, sunshine
- Wind direction and speed (gust, 9am, 3pm)
- Humidity and pressure (9am, 3pm)
- Cloud cover (9am, 3pm)
- `RainToday` and `RainTomorrow` (target variable)

---

## Methodology

### 1. Data Exploration (EDA)
- Loaded the dataset with pandas
- Visualized missing values with a seaborn heatmap
- Rule applied: if a column has too much missing data (~35%+), drop it, otherwise the model becomes unreliable

### 2. Data Cleaning & Preprocessing
- **Dropped columns with heavy missingness:** `Evaporation`, `Sunshine`, `Cloud9am`, `Cloud3pm`
- **Dropped rows** where the target (`RainTomorrow`) was missing
- **Numeric gaps:** filled with the column median
- **Categorical gaps:** filled with the column mode
- **Date handling:** converted `Date` to datetime, extracted a `Months` feature, then dropped `Date`
- **Binary encoding:** `RainToday` and `RainTomorrow` mapped Yes → 1, No → 0
- **Train-test split:** 80-20 (`random_state=43`)
- **Encoding and scaling:** `ColumnTransformer` with `OneHotEncoder` for categorical columns and `StandardScaler` for numeric columns (107 features after encoding)

### 3. Model Development
- **Algorithm:** Logistic Regression (`max_iter=1000`)
- **Imbalance handling:** SMOTE (`random_state=42`) oversamples the minority (rain) class
- **Pipeline:** Preprocessing → SMOTE → Logistic Regression, built with `imblearn.pipeline.Pipeline`, so SMOTE is applied only to training data during fitting and never to the test set

### 4. Evaluation Metrics
- **Accuracy:** Overall correctness
- **Precision:** Of predicted rainy days, how many were truly rainy
- **Recall:** Of truly rainy days, how many were caught
- **F1-Score:** Balance between precision and recall
- **ROC-AUC:** Model discrimination ability
- **Confusion Matrix:** Detailed performance breakdown

---

## Key Findings

### A. Class Distribution
- **No Rain (0):** 22,064 test samples (~78%)
- **Rain (1):** 6,375 test samples (~22%)
- **Imbalance issue:** Rainy days are the minority class, so plain accuracy would be misleading. SMOTE and per-class metrics were used to address this.

### B. Model Performance

| Metric | Value |
|---|---|
| Accuracy | 79.00% |
| ROC-AUC | 0.860 |
| Test set size | 28,439 |

### C. Confusion Matrix

| | Predicted No Rain | Predicted Rain |
|---|---|---|
| **Actual No Rain** | 17,603 | 4,461 |
| **Actual Rain** | 1,511 | 4,864 |

### D. Classification Report

| Class | Precision | Recall | F1-Score | Support |
|---|---|---|---|---|
| No Rain (0) | 0.92 | 0.80 | 0.85 | 22,064 |
| Rain (1) | 0.52 | 0.76 | 0.62 | 6,375 |
| Macro avg | 0.72 | 0.78 | 0.74 | 28,439 |
| Weighted avg | 0.83 | 0.79 | 0.80 | 28,439 |

### E. Insights

**Strengths:**
- Recall for rainy days is high (0.76): the model catches about 3 in 4 rainy days
- Precision for dry days is high (0.92): a "No Rain" prediction is usually trustworthy
- AUC of 0.86 shows good separation between rainy and dry days across thresholds

**Weaknesses:**
- Precision for rainy days is low (0.52): about half of the "Rain" alerts are false alarms (4,461 false positives)
- This is the expected trade-off of SMOTE: recall on the minority class goes up, precision goes down

### F. Example Prediction

A custom "new day" was built by editing a template row (MinTemp 15.2, MaxTemp 26.5, Rainfall 0.0, Humidity3pm 65.0, Pressure3pm 1010.2):
- **Probability of rain tomorrow:** 63.43%
- **Final forecast:** Rain tomorrow

---

## Visualizations Generated

1. **Missing Data Heatmap:** Shows which columns have heavy missingness
2. **ROC Curve:** Model discrimination against the random-guess baseline (AUC = 0.86)

---

## Limitations & Possible Improvements

1. **Threshold tuning:** The default 0.5 cutoff gives many false alarms. Choose a threshold that matches the cost of a missed rainy day versus a false alarm.
2. **Imputation before splitting:** Medians and modes were computed on the full dataset before the train-test split, which leaks a small amount of information. Move imputation into the pipeline.
3. **Month as a number:** `Months` is treated as a plain number, but December and January are adjacent. Cyclical (sin/cos) encoding or one-hot encoding would capture seasonality better.
4. **Time-aware split:** Weather data is a time series. A chronological split is a more realistic test than a random one.
5. **Stronger models:** Try Random Forest, XGBoost, or LightGBM and compare with `class_weight` as an alternative to SMOTE.
6. **Feature engineering:** Add differences such as humidity change (9am → 3pm) and pressure change, and lagged features from previous days.

---

## Agricultural Connection

### How This Applies to Farming:

1. **Irrigation Planning:**
   - Skip or delay irrigation when rain is likely tomorrow
   - Save water, energy, and labor

2. **Field Operations Timing:**
   - Schedule spraying, fertilizer application, and harvesting on dry days
   - Avoid nutrient and pesticide loss from runoff

3. **Crop Risk Management:**
   - Give early warning for heavy rain in flood- or waterlogging-prone rice systems
   - Support decisions on drainage and harvest timing

4. **Integration with Remote Sensing:**
   - Combine rainfall forecasts with satellite indices such as NDVI (Sentinel-2) and SAR-based flood detection (Sentinel-1)
   - Interpret vegetation anomalies with weather context

---

## Skills Demonstrated

✅ Exploratory Data Analysis (EDA) and missing-data visualization  
✅ Data cleaning (median/mode imputation, column and row dropping)  
✅ Feature engineering (month extraction from dates)  
✅ Categorical encoding (One-Hot) and scaling (StandardScaler)  
✅ Pipelines with `ColumnTransformer`  
✅ Handling class imbalance with SMOTE  
✅ Logistic regression modeling  
✅ Model evaluation (confusion matrix, classification report, ROC-AUC)  
✅ Single-sample prediction and probability interpretation  
✅ Agricultural domain mapping  

---

**Last Updated:** September 2026
