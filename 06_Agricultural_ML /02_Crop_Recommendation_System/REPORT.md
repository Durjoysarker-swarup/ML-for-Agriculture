# Crop Recommendation — Detailed Report

## Executive Summary

This project recommends the most suitable crop for a field based on soil nutrients (N, P, K), soil pH, and local climate (temperature, humidity, rainfall). Two multi-class classifiers were compared: a Decision Tree (~98.0% accuracy) and a Random Forest (~99.3% accuracy). The Random Forest made only 3 errors out of 440 test samples.

---

## Problem Statement

**Objective:** Build a classifier that recommends one of 22 crops from soil and climate conditions

**Practical Impact:** Data-driven crop selection helps farmers choose crops that match their soil and climate, reducing input waste and crop failure risk

**Dataset:** `Crop_recommendation.csv`, 2,200 records × 8 columns:
- `N`, `P`, `K`: nitrogen, phosphorus, and potassium content in soil
- `temperature`: temperature (°C)
- `humidity`: relative humidity (%)
- `ph`: soil pH
- `rainfall`: rainfall (mm)
- `label`: recommended crop (target variable, 22 classes)

---

## Methodology

### 1. Data Inspection & Quality Audit
- Checked column names, data types, and non-null counts (`df.info()`)
- Built a quality report: missing values, unique values, and data types
- Checked duplicate rows
- Reviewed descriptive statistics
- Checked physical plausibility of features (for example, the pH range)

### 2. Exploratory Data Analysis (EDA)
- Counted crop classes and plotted class balance
- Computed the average growing conditions for each crop
- Identified the crop with the highest mean requirement for each feature

### 3. Data Preparation
- **Features (X):** N, P, K, temperature, humidity, ph, rainfall
- **Target (y):** `label`
- **Train-test split:** 80-20, stratified by crop (`random_state=42`), giving 1,760 training and 440 test rows (20 per crop in the test set)
- Exported training and test sets to CSV

### 4. Model Development
- **Decision Tree Classifier:** default settings (`random_state=42`)
- **Random Forest Classifier:** `n_estimators=300`, `n_jobs=-1`, `random_state=42`

### 5. Evaluation Metrics
- **Accuracy:** Overall correctness
- **Confusion Matrix:** Which crops get confused with which
- **Precision, Recall, F1-Score:** Per-crop performance

---

## Key Findings

### A. Data Quality
- 2,200 rows, 0 missing values, 0 duplicate rows
- 22 crops, each with exactly 100 samples, so the classes are perfectly balanced
- pH ranges from 3.50 to 9.94, which is a plausible soil range

| Feature | Min | Mean | Max |
|---|---|---|---|
| N | 0 | 50.6 | 140 |
| P | 5 | 53.4 | 145 |
| K | 5 | 48.1 | 205 |
| Temperature (°C) | 8.8 | 25.6 | 43.7 |
| Humidity (%) | 14.3 | 71.5 | 100.0 |
| pH | 3.5 | 6.5 | 9.9 |
| Rainfall (mm) | 20.2 | 103.5 | 298.6 |

### B. Crop Profiles

Crops with the highest average requirement for each feature:

| Feature | Crop | Mean value |
|---|---|---|
| Nitrogen (N) | Cotton | 117.77 |
| Phosphorus (P) | Apple | 134.22 |
| Potassium (K) | Grapes | 200.11 |
| Temperature | Papaya | 33.72 °C |
| Humidity | Coconut | 94.84 % |
| pH | Chickpea | 7.34 |
| Rainfall | Rice | 236.18 mm |

Fruit crops such as apple and grapes stand out for very high P and K, while rice stands out for very high rainfall.

### C. Decision Tree Performance

| Metric | Value |
|---|---|
| Accuracy | 97.95% |
| Macro avg F1 | 0.98 |
| Test size | 440 |

**Weakest classes:**

| Crop | Precision | Recall | F1 |
|---|---|---|---|
| Blackgram | 1.00 | 0.80 | 0.89 |
| Lentil | 0.86 | 0.90 | 0.88 |
| Mothbeans | 0.86 | 0.95 | 0.90 |
| Jute | 0.95 | 0.95 | 0.95 |
| Rice | 0.95 | 0.95 | 0.95 |

Most crops (16 of 22) reached perfect precision and recall.

### D. Random Forest Performance

| Metric | Value |
|---|---|
| Accuracy | 99.32% |
| Macro avg F1 | 0.99 |
| Test size | 440 |

- Only **3 misclassifications** in total: one blackgram → maize, one lentil → mothbeans, and one rice → jute
- Improves on the single tree by about 1.4 percentage points (from ~9 errors to 3)

### E. Model Comparison

| Model | Accuracy | Errors (of 440) |
|---|---|---|
| Decision Tree | 97.95% | 9 |
| Random Forest (300 trees) | **99.32%** | **3** |

### F. Example Recommendation

Input: N = 90, P = 42, K = 43, temperature = 20 °C, humidity = 80%, pH = 6.5, rainfall = 200 mm
- **Recommended crop (Random Forest): Rice**

---

## Visualizations Generated

1. **Class Balance:** Horizontal bar chart showing 100 samples per crop
2. **Confusion Matrices:** For the Decision Tree and the Random Forest, showing where crops get confused

---

## Limitations & Possible Improvements

1. **Suspiciously high accuracy:** Near-perfect scores suggest that the crop classes are cleanly separated, likely because the dataset is curated or idealized. Real farm data is noisier, so expect lower accuracy in practice.
2. **Single train-test split:** Use stratified k-fold cross-validation to get a more reliable estimate.
3. **Similar crops get confused:** Blackgram, lentil, mothbeans, and mungbean have similar profiles, as do rice and jute. Use probabilities or top-3 recommendations rather than a single hard label.
4. **Feature importance not examined:** Random Forest importances or permutation importance would show which variables drive recommendations.
5. **Missing real-world factors:** Soil type, season, irrigation, market price, and local suitability are not in the data.
6. **Top-3 recommendations:** The notebook computes `predict_proba` for a single case; sorting these probabilities gives ranked alternatives, which is more useful for farmers.
7. **Hyperparameter tuning:** Limit tree depth, and tune the forest with `GridSearchCV` to check robustness.

---

## Agricultural Connection

### How This Applies to Farming:

1. **Crop Selection Support:**
   - Match crops to soil nutrients, pH, and climate before planting
   - Reduce the risk of planting an unsuitable crop

2. **Fertilizer Planning:**
   - Crop profiles show very different nutrient needs (for example, cotton needs high N and grapes need high K)
   - Guide targeted fertilizer use and avoid over-application

3. **Climate-Based Decisions:**
   - Rice is associated with the highest rainfall (~236 mm) in this dataset, consistent with monsoon-fed rice systems
   - Scenario testing ("what if rainfall or temperature shifts?") supports climate adaptation planning

4. **Integration with GIS and Remote Sensing:**
   - Pair a crop recommender with GIS layers (soil maps, rainfall grids) and satellite-derived indicators from Sentinel-2 and Sentinel-1
   - Produce spatial crop suitability maps for a region

---

## Skills Demonstrated

✅ Data quality auditing (missing values, duplicates, unique counts, plausibility checks)  
✅ Exploratory Data Analysis (EDA) and class-balance visualization  
✅ Group-wise feature profiling (`groupby` and `idxmax`)  
✅ Stratified train-test splitting  
✅ Decision Tree and Random Forest classification  
✅ Multi-class evaluation (accuracy, confusion matrix, classification report)  
✅ Single-case prediction and probability outputs  
✅ Agricultural domain mapping  

---

**Last Updated:** September 2026
