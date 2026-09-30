# Crop Yield Prediction — Detailed Report

## Executive Summary

This project predicts cereal yield (t/ha) from fertilizer use, annual rainfall, and average temperature. Three models of increasing complexity were compared: Linear Regression (baseline), Decision Tree, and Random Forest. Random Forest performed best (R² ≈ 0.58, MAE ≈ 0.80 t/ha), well ahead of the linear baseline (R² ≈ 0.22).

---

## Problem Statement

**Objective:** Build a regression model that estimates cereal yield from fertilizer, rainfall, and temperature

**Practical Impact:** Yield estimates support input planning (fertilizer), risk assessment under climate variability, and food security analysis

**Dataset:** `Yield.csv`, 9,168 records × 7 columns (country-year data, 1961–2023):
- `Entity`, `Code`, `Year`: country name, ISO code, year
- `yield_t_ha`: cereal yield in tonnes per hectare (target variable)
- `fertilizer_kg_ha`: fertilizer use (kg/ha)
- `rainfall_mm`: annual rainfall (mm)
- `temperature_c`: average annual temperature (°C)

---

## Methodology

### 1. Data Exploration (EDA)
- Loaded the dataset and inspected its structure
- Scatter plots of yield against each predictor (fertilizer, rainfall, temperature)
- Correlation matrix of yield and the three predictors

### 2. Data Preparation
- **Features (X):** `fertilizer_kg_ha`, `rainfall_mm`, `temperature_c`
- **Target (y):** `yield_t_ha`
- **Train-test split:** 80-20 (7,334 training / 1,834 test rows, `random_state=0`)

### 3. Model Development
- **Baseline: Linear Regression:** fitted with scikit-learn and cross-checked with `statsmodels` OLS to obtain p-values and diagnostics
- **Decision Tree Regressor:** `max_depth=3`, `min_samples_leaf=50` (limits overfitting)
- **Random Forest Regressor:** `n_estimators=500`, `max_depth=10`, `min_samples_leaf=30`, `n_jobs=-1`

### 4. Evaluation Metrics
- **MAE:** Average absolute error in t/ha (lower is better)
- **RMSE:** Square root of the mean squared error; penalizes large errors more
- **R²:** Share of yield variability explained by the model

---

## Key Findings

### A. Correlation Analysis

| | Yield | Fertilizer | Rainfall | Temperature |
|---|---|---|---|---|
| **Yield** | 1.000 | 0.454 | −0.005 | −0.230 |
| **Fertilizer** | 0.454 | 1.000 | 0.093 | −0.158 |
| **Rainfall** | −0.005 | 0.093 | 1.000 | 0.182 |
| **Temperature** | −0.230 | −0.158 | 0.182 | 1.000 |

- Fertilizer has the strongest positive relationship with yield
- Temperature has a moderate negative relationship
- Rainfall shows almost no *linear* relationship, though the scatter plot suggests a non-linear pattern

### B. Baseline Linear Regression

| Metric | Value |
|---|---|
| MAE | 1.22 |
| RMSE | 2.22 |
| R² | 0.22 |

**OLS results:**

| Term | Coefficient | p-value | Significant? |
|---|---|---|---|
| Constant | 3.0480 | 0.000 | Yes |
| Fertilizer (kg/ha) | 0.0045 | 0.000 | Yes |
| Rainfall (mm) | −0.00005 | 0.077 | No (at 5%) |
| Temperature (°C) | −0.0488 | 0.000 | Yes |

- Overall model is significant (F = 923.5, p < 0.05), but explains only ~23% of yield variability (Adj. R² = 0.232)
- Each extra kg/ha of fertilizer adds ~0.0045 t/ha of yield; each extra °C lowers yield by ~0.05 t/ha
- Rainfall is not statistically significant in the linear model
- The constant (yield at 0 fertilizer, 0 mm, 0 °C) is not physically meaningful

**Diagnostics (warnings):**
- Condition number is large (4.27e3), pointing to possible multicollinearity or scaling issues
- Residuals are strongly non-normal (skew 5.6, kurtosis 64.2) and autocorrelated (Durbin-Watson 0.20), so linear model assumptions are not met

### C. Decision Tree Regression

| Metric | Value |
|---|---|
| MAE | 1.00 |
| RMSE | 1.85 |
| R² | 0.46 |

- Roughly doubles the explained variability compared with the linear baseline
- The first split is on fertilizer use (about 89 kg/ha), followed by further splits on fertilizer, temperature, and rainfall
- A small group of high-input observations (52 samples) forms a leaf with a very high average yield (~14.3 t/ha)

### D. Random Forest Regression

| Metric | Value |
|---|---|
| MAE | 0.80 |
| RMSE | 1.63 |
| R² | 0.58 |

- Best model of the three: lowest errors and highest R²
- Captures non-linear effects and interactions that linear regression misses

### E. Model Comparison

| Model | MAE | RMSE | R² |
|---|---|---|---|
| Linear Regression | 1.22 | 2.22 | 0.22 |
| Decision Tree (depth 3) | 1.00 | 1.85 | 0.46 |
| Random Forest | **0.80** | **1.63** | **0.58** |

### F. Example Prediction

The Random Forest was used to predict yield for two hypothetical scenarios:
1. Fertilizer 100 kg/ha, rainfall 1,400 mm, temperature 25 °C
2. Fertilizer 1,500 kg/ha, rainfall 1,000 mm, temperature 30 °C

The second scenario uses an extreme fertilizer rate, so its prediction should be treated with caution (see limitations).

---

## Visualizations Generated

1. **Yield vs. Fertilizer:** Scatter plot showing a positive but noisy relationship
2. **Yield vs. Rainfall:** Scatter plot showing no clear linear trend
3. **Yield vs. Temperature:** Scatter plot showing distinct temperature clusters
4. **Decision Tree Diagram:** Splits and average yield in each leaf

---

## Limitations & Possible Improvements

1. **Mislabeled tree plot:** `feature_names` was set in a different order (`rainfall, temperature, fertilizer`) from the columns of `X` (`fertilizer, rainfall, temperature`). The tree diagram therefore shows the wrong feature names. Use `feature_names=X.columns` to fix it.
2. **Random split on panel data:** The same country appears in many years, so a random split lets similar rows land in both train and test. Group by country (`GroupKFold`) or split by year for a more honest estimate.
3. **Missing context variables:** Country, year (technology trend), crop type, soil, and irrigation are not used. Adding `Year` or country effects would likely raise R².
4. **Skewed target and outliers:** Yield is heavily right-skewed. Try a log transform or robust metrics.
5. **RMSE vs. MAE note:** RMSE is always greater than or equal to MAE, so the comparison rule "RMSE < MAE means satisfactory" cannot hold. Judge errors against the yield range and against a naive baseline (predicting the mean).
6. **Tuning and validation:** Use cross-validation and hyperparameter search (`GridSearchCV`); also try Gradient Boosting or XGBoost and check feature importances.
7. **Extrapolation:** Predictions far outside the training range (such as very high fertilizer rates) are unreliable for tree-based models.

---

## Agricultural Connection

### How This Applies to Farming:

1. **Fertilizer Management:**
   - Yield rises with fertilizer, but the relationship is non-linear and noisy
   - Models like this help identify diminishing returns and avoid over-application

2. **Climate Risk Assessment:**
   - Higher average temperature is associated with lower yield
   - Rainfall effects depend on context, which is why non-linear models outperform the linear baseline

3. **Regional Planning:**
   - Scenario testing ("what if fertilizer or temperature changes?") supports input planning and adaptation strategies

4. **Integration with Remote Sensing:**
   - Adding satellite-derived variables (NDVI from Sentinel-2, SAR backscatter from Sentinel-1) to weather and input data could improve field- and district-level yield prediction, for example in monsoon-affected rice systems

---

## Skills Demonstrated

✅ Exploratory Data Analysis (EDA) and scatter-plot visualization  
✅ Correlation analysis  
✅ Train-test splitting  
✅ Linear regression (scikit-learn and statsmodels OLS)  
✅ Interpretation of coefficients, p-values, F-statistic, and diagnostics  
✅ Decision Tree and Random Forest regression  
✅ Regression metrics (MAE, RMSE, R²)  
✅ Model comparison  
✅ Single- and multi-scenario prediction  
✅ Agricultural domain mapping  

---

**Last Updated:** September 2026
