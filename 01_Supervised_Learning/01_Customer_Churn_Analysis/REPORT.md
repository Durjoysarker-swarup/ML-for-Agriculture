# Customer Churn Analysis — Detailed Report

## Executive Summary

This project analyzes a telecom customer churn dataset to identify patterns that predict customer departure. Using logistic regression and exploratory analysis, we identify key factors driving customer loss and provide actionable insights.

---

## Problem Statement

**Objective:** Build a predictive model to identify customers likely to churn (leave the service)

**Business Impact:** By identifying at-risk customers early, companies can implement retention strategies

**Dataset:** Telecom customer records with 10,000 customers and 21 features including:
- Demographics (age, gender, location)
- Service usage patterns
- Contract details
- Billing information
- Churn status (target variable)

---

## Methodology

### 1. Data Exploration (EDA)
- Dataset shape and structure
- Missing values analysis
- Feature distributions
- Churn rate analysis

### 2. Data Preprocessing
- Handling missing values
- Encoding categorical variables
- Feature scaling (standardization)
- Train-test split (80-20)

### 3. Model Development
- **Algorithm:** Logistic Regression
- **Features:** Scaled numerical and encoded categorical variables
- **Training:** Standard scaling + logistic regression

### 4. Evaluation Metrics
- **Accuracy:** Overall correctness
- **Precision:** Accuracy of positive predictions
- **Recall:** Ability to identify all churners
- **F1-Score:** Balance between precision and recall
- **ROC-AUC:** Model discrimination ability
- **Confusion Matrix:** Detailed performance breakdown

---

## Key Findings

### A. Churn Distribution
- **Overall churn rate:** ~27% of customers churn
- **Retention rate:** ~73% of customers stay
- **Imbalance issue:** Class imbalance present (handled through appropriate metrics)

### B. Feature Importance
Top factors predicting churn:
1. **Contract type** — Month-to-month contracts have much higher churn
2. **Tenure** — Newer customers are more likely to churn
3. **Monthly charges** — Higher charges correlate with churn
4. **Internet service type** — Fiber optic customers churn more
5. **Tech support** — Customers without tech support churn more

### C. Model Performance
- **Accuracy:** ~80%
- **Precision:** ~67% (When we predict churn, we're right 67% of the time)
- **Recall:** ~65% (We identify 65% of actual churners)
- **ROC-AUC:** ~0.85 (Good discrimination between churners and non-churners)

### D. Insights by Customer Segment

**High-Risk Segments:**
- New customers (< 3 months)
- Month-to-month contract holders
- Fiber optic internet users without tech support
- Monthly charges > $80

**Low-Risk Segments:**
- Long-tenure customers (> 1 year)
- 2-year contract holders
- Tech support subscribers
- Multiple service bundles

---

## Visualizations Generated

1. **Churn Distribution** — Bar plot showing churn vs. retention rates
2. **Feature Distributions** — Histograms of key variables
3. **Churn by Contract Type** — Comparison of churn rates across contract types
4. **Tenure Analysis** — Churn rate vs. customer tenure
5. **Monthly Charges vs. Churn** — Relationship between billing and churn
6. **Confusion Matrix** — Model predictions breakdown
7. **ROC Curve** — Model discrimination visualization

---

## Agricultural Connection

### How This Applies to Farming:

1. **Farmer Retention Programs:**
   - Identify which farmers drop out of climate-smart agriculture programs
   - Understand which training programs are most effective
   - Determine optimal timing for intervention

2. **Extension Service Effectiveness:**
   - Predict which farmers will abandon recommended practices
   - Identify barriers to adoption (cost, complexity, trust)
   - Design retention strategies

3. **Program Design:**
   - New farmers (like new telecom customers) need more support
   - Flexible, short-term options have higher failure rates
   - Bundled services (like tech support) improve retention

4. **Resource Allocation:**
   - Focus retention efforts on high-value farmers
   - Prioritize support for early adoption phases
   - Create targeted interventions for at-risk segments

---

## Recommendations

### 1. For Telecom Business
- **Target Interventions:** Focus on month-to-month customers in first 3 months
- **Enhance Tech Support:** Major factor in retention
- **Pricing Strategy:** Consider discounts for high-monthly-charge customers
- **Bundling:** Promote multi-service packages (shown to reduce churn)

### 2. For Agricultural Applications
- **Early Support:** Intensive engagement in first season with new farmers
- **Long-term Programs:** Shift from month-to-month to season-based or annual commitments
- **Technical Support:** Provide strong extension support (equivalent to tech support)
- **Integrated Services:** Bundle crop recommendation, monitoring, and market access

---

## Model Limitations

1. **Class Imbalance:** 27% churn rate may affect model performance; consider SMOTE or class weights for improvement
2. **Temporal Aspects:** Static snapshot; doesn't account for seasonal patterns
3. **External Factors:** Macroeconomic conditions not captured
4. **Generalization:** Model trained on specific telecom company; may not transfer to other industries

---

## Next Steps

1. **Improved Models:** Test random forest, XGBoost for better performance
2. **Feature Engineering:** Create interaction terms, temporal features
3. **Threshold Tuning:** Adjust decision threshold based on business costs
4. **A/B Testing:** Test retention strategies on identified high-risk customers
5. **Integration:** Combine with other customer data for deeper insights

---

## Skills Demonstrated

✅ Exploratory Data Analysis (EDA)  
✅ Data visualization (matplotlib, seaborn)  
✅ Feature scaling and normalization  
✅ Logistic regression from first principles  
✅ Model evaluation metrics  
✅ Interpretation of model results  
✅ Business insight generation  
✅ Agricultural domain mapping  

---

## References

- Dataset: Telecom churn dataset (UCI Machine Learning Repository)
- Techniques: Binary classification, logistic regression
- Metrics: Standard classification evaluation approaches

---

**Last Updated:** June 2026
