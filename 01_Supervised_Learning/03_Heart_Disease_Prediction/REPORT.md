# Heart Disease Prediction — Detailed Report

## Executive Summary

This project develops and compares classification models to predict heart disease from clinical measurements. By comparing logistic regression (simple, interpretable) with random forest (complex, ensemble), we demonstrate how different algorithmic approaches reveal different insights about the data.

---

## Problem Statement

**Objective:** Predict presence of heart disease from patient clinical measurements

**Clinical Significance:** Heart disease is leading cause of death; early detection enables intervention

**Dataset:** Heart Disease Dataset
- 303 patients from Cleveland, Hungary, Switzerland, Long Beach
- 13 clinical features (age, sex, chest pain type, blood pressure, etc.)
- Target: Presence of heart disease (binary)

---

## Methodology

### 1. Data Exploration
- Patient demographics and clinical measurements
- Feature distributions by disease status
- Correlation analysis
- Missing value assessment

### 2. Data Preprocessing
- Handling missing values
- Feature scaling (important for distance-based algorithms)
- Train-test split (80-20, stratified)

### 3. Model Development

**Model 1: Logistic Regression**
- Simple, interpretable model
- Provides probability estimates
- Works well with scaled features

**Model 2: Random Forest**
- Ensemble method (multiple decision trees)
- Handles non-linear relationships
- Provides feature importance
- More complex but potentially more accurate

### 4. Evaluation
- Accuracy, precision, recall, F1-score
- ROC-AUC curves
- Cross-validation (5-fold)
- Feature importance comparison

---

## Key Findings

### A. Model Performance Comparison

**Logistic Regression:**
- **Accuracy:** ~85%
- **Sensitivity:** ~91%
- **Specificity:** ~77%
- **Interpretability:** High (linear relationships)

**Random Forest:**
- **Accuracy:** ~83%
- **Sensitivity:** ~85%
- **Specificity:** ~81%
- **Interpretability:** Moderate (feature importance available)

**Comparison:**
Logistic Regression achieves ~2% higher accuracy.
### B. Feature Importance Analysis

**Top Predictors (Random Forest):**
1. ST depression — Most important (non-linear effects)
2. Maximum heart rate
3. Chest pain type
4. Age
5. Vessels involved in blockage


---

## Agricultural Connection

### How This Applies to Farming:

1. **Yield Prediction Algorithms:**
   - **Simple models** (linear regression): Work when relationships are straightforward
   - **Complex models** (random forest): Better for complex crop-environment interactions
   - **Ensemble methods**: Combine satellite, weather, soil data for robust predictions

2. **Feature Importance for Farming:**
   - Identify which factors truly drive yields vs. correlated proxies
   - Different models reveal different insights
   - Agricultural advice should highlight top drivers

3. **Interpretability vs. Accuracy:**
   - Farmers want to understand why a recommendation is made
   - More complex models may achieve better accuracy but lose interpretability
   - Hybrid approach: Use complex models for predictions, explain with simpler models

4. **Sensor Data Integration:**
   - Like clinical measurements → disease prediction
   - Multiple farm sensors → crop health/yield prediction
   - Ensemble of sensor data more reliable than single measurement

---

## Skills Demonstrated

✅ Algorithm comparison and evaluation  
✅ Logistic regression fundamentals  
✅ Random forests and ensemble methods  
✅ Feature importance analysis  
✅ Cross-validation for model stability  
✅ Clinical data understanding  
✅ Interpretability vs. accuracy tradeoff  
✅ Agricultural model application  

---

**Last Updated:** June 2026
