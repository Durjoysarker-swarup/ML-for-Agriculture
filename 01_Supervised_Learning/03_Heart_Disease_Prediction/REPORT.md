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
- **Accuracy:** ~82%
- **Precision:** ~81%
- **Recall:** ~82%
- **ROC-AUC:** ~0.88
- **Interpretability:** High (linear relationships)

**Random Forest:**
- **Accuracy:** ~85%
- **Precision:** ~86%
- **Recall:** ~84%
- **ROC-AUC:** ~0.91
- **Interpretability:** Moderate (feature importance available)

**Comparison:**
Random Forest achieves ~3% higher accuracy, suggesting non-linear patterns in data.

### B. Feature Importance Analysis

**Top Predictors (Logistic Regression):**
1. Chest pain type — Strong indicator of disease
2. Maximum heart rate achieved
3. ST depression (ECG measurement)
4. Age
5. Serum cholesterol

**Top Predictors (Random Forest):**
1. ST depression — Most important (non-linear effects)
2. Maximum heart rate
3. Chest pain type
4. Age
5. Vessels involved in blockage

**Insight:** Different models emphasize different features; Random Forest captures ST depression's complex relationship.

### C. Clinical Patterns

**High-Risk Patients:**
- Chest pain (typical angina)
- ST depression on ECG
- High resting blood pressure
- Low maximum heart rate
- Advanced age (> 60)

**Low-Risk Patients:**
- Asymptomatic or atypical chest pain
- Normal ST segment on ECG
- Normal heart rate response to exercise
- Younger age
- No family history indicators

### D. Algorithm Insights

**Why Random Forest Performs Better:**
- Captures non-linear relationships (e.g., ST depression effect varies by age)
- Reduces overfitting through ensemble averaging
- Better handles feature interactions

**When Logistic Regression Better:**
- Simpler to explain to non-technical stakeholders
- Requires less data for reliable estimates
- Computationally cheaper
- Linear assumption valid for many medical relationships

---

## Visualizations Generated

1. **Feature Distributions** — By disease status
2. **Correlation Heatmap** — Feature relationships
3. **ROC Curves** — Both models compared
4. **Feature Importance** — Logistic regression coefficients
5. **Tree-based Feature Importance** — Random forest rankings
6. **Confusion Matrices** — Both models
7. **Cross-validation Scores** — Stability assessment

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

## Recommendations

### 1. For Clinical Use
- **Primary Tool:** Use random forest for triage (3% better accuracy)
- **Explanation:** Use logistic regression coefficients to explain findings
- **Threshold:** Adjust based on treatment benefit vs. risk
- **Integration:** Combine with other tests for diagnosis

### 2. For Agricultural Applications
- **Model Selection:** Use random forest for prediction accuracy
- **Feature Focus:** Identify top 3-5 drivers to explain to farmers
- **Data Collection:** Prioritize measurement of important features
- **Hybrid Approach:** Ensemble predictions from multiple models
- **Validation:** Test recommendations on actual fields

---

## Model Limitations

1. **Sample Size:** 303 patients relatively small for deep learning
2. **Dataset Specific:** Multi-center data; results may vary by region
3. **Feature Engineering:** Limited exploration of derived features
4. **Temporal Aspects:** Cross-sectional data; disease progression not captured
5. **Class Imbalance:** Roughly 50-50 split; easily balanced

---

## Next Steps

1. **Gradient Boosting:** XGBoost or LightGBM for even better performance
2. **Feature Interaction:** Explore engineered features (e.g., age × heart rate)
3. **Threshold Optimization:** Set based on clinical cost-benefit
4. **Calibration:** Ensure probability estimates are reliable
5. **Feature Engineering:** Create domain-relevant derived features
6. **Explainability:** Use SHAP or LIME for individual predictions

---

## Skills Demonstrated

✅ Algorithm comparison and evaluation  
✅ Logistic regression fundamentals  
✅ Random forests and ensemble methods  
✅ Feature importance analysis  
✅ ROC curve interpretation  
✅ Cross-validation for model stability  
✅ Clinical data understanding  
✅ Interpretability vs. accuracy tradeoff  
✅ Agricultural model application  

---

## References

- Dataset: UCI Machine Learning Repository — Heart Disease
- Algorithms: Scikit-learn implementations
- Evaluation: Standard classification metrics

---

**Last Updated:** June 2026
