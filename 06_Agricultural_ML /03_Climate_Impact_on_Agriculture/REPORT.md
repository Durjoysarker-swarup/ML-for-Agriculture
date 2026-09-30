# Report: Time Series Analysis of Crop Yield vs Climate

## 1. Objective

To analyze the relationship between crop yield and two climate variables — average temperature and annual rainfall — using time series data spanning 1981 to 2024, and to test whether these climate variables can help explain or predict crop yield.

## 2. Dataset

The dataset contains 44 yearly observations (1981–2024) with the following variables:

- `year` — year of observation
- `yield_kg_ha` — crop yield (kg/ha)
- `avg_temp_c` — average temperature (°C)
- `annual_rainfall_mm` — annual rainfall (mm)

## 3. Exploratory Visualization

Plotting the three raw series over time showed:

- **Crop Yield** — a strong, steady upward trend from ~1,900 kg/ha in 1981 to over 5,000 kg/ha by 2024, with no clear seasonality, suggesting the trend is likely driven by long-term factors such as improved agricultural technology or practices rather than climate alone.
- **Average Temperature** — a fluctuating series with no strong long-term trend, ranging roughly between 25°C and 27°C.
- **Annual Rainfall** — mostly fluctuating between 1,000–2,000 mm, with a sharp spike around 2017 (~5,000 mm) before returning to typical levels.

## 4. Detrending via First Differencing

Since crop yield showed a strong trend, raw-level correlations between yield and climate variables would be misleading (both yield and time are correlated, which can create spurious relationships). To address this, first differences (year-over-year changes) were computed for all three variables.

**Correlation of year-over-year changes:**

| | Δ Yield | Δ Temperature | Δ Rainfall |
|---|---|---|---|
| **Δ Yield** | 1.000 | 0.209 | -0.329 |
| **Δ Temperature** | 0.209 | 1.000 | -0.439 |
| **Δ Rainfall** | -0.329 | -0.439 | 1.000 |

**Interpretation:**
- Yield changes are **weakly positively correlated** with temperature changes (0.21) — warmer-than-usual years show a slight tendency toward higher yield growth, though the relationship is weak.
- Yield changes are **weakly negatively correlated** with rainfall changes (-0.33) — years with above-average rainfall increases show a mild tendency toward lower yield growth.
- Temperature and rainfall changes are themselves negatively correlated (-0.44).

## 5. Stationarity Testing (Augmented Dickey-Fuller Test)

| Series | p-value (raw) | p-value (differenced) |
|---|---|---|
| Yield | 0.987 | 2.30e-09 |
| Temperature | 0.400 | 3.87e-19 |
| Rainfall | 0.531 | 2.37e-16 |

**Interpretation:** None of the raw series are stationary (p > 0.05 in all cases), confirming the presence of trends/persistence. After first differencing, all series become strongly stationary (p << 0.05), justifying the use of differenced data for correlation analysis and motivating the differencing order used in the SARIMAX model.

## 6. Autocorrelation of Crop Yield

The ACF plot of raw yield shows high, slowly-decaying autocorrelation (starting near 1.0 and decreasing gradually through lag 10, staying outside the confidence band for several lags). This indicates strong year-to-year persistence in yield — consistent with the pronounced upward trend observed earlier and reinforcing the need for differencing before modeling.

## 7. Climate Relationships (Raw vs. Differenced)

- **Raw levels:** Scatter plots of yield vs. temperature and yield vs. rainfall show visible patterns, but these are confounded by the shared upward trend over time (i.e., yield is high in most recent years regardless of climate).
- **Differenced (year-over-year changes):** Scatter plots of Δyield vs. Δtemperature and Δyield vs. Δrainfall show much weaker, noisier relationships — consistent with the low correlation coefficients found above. This suggests that most of the apparent raw-level relationship is driven by shared trends rather than a direct causal link between short-term climate fluctuations and yield changes.

## 8. SARIMAX Modeling

Three SARIMAX specifications were tested using `yield_kg_ha` as the dependent variable and `avg_temp_c`, `annual_rainfall_mm` as exogenous regressors:

### Model 1: SARIMAX(1,1,0) with trend='ct'
- AIC: 526.97
- `annual_rainfall_mm` coefficient significant (p = 0.043), negative sign (-0.053)
- `avg_temp_c` not significant (p = 0.579)
- AR(1) term not significant (p = 0.956)

### Model 2: SARIMAX(1,0,0) with trend='ct'
- AIC: 558.07 (worse fit than Model 1)
- `avg_temp_c` significant (p < 0.001), positive (236.76)
- AR(1) term significant (p < 0.001, coefficient 0.89) — reflecting the strong persistence in the undifferenced series
- Convergence warning raised during fitting

### Model 3: SARIMAX(0,1,0) with trend='ct'
- (Model fit, results consistent with the differenced approach; removes autoregressive term entirely)

**Interpretation:** The differenced model (Model 1) is preferred, since it operates on stationary data and has the lowest AIC among the tested models. Its results suggest rainfall has a modest, statistically significant negative association with yield changes once trend is accounted for, while temperature's effect is not statistically significant in this specification. The non-differenced model (Model 2) shows a significant positive temperature effect, but this is likely confounded by the shared trend between yield and time, and its convergence warning further reduces confidence in these estimates.

## 9. Key Takeaways

1. Crop yield has grown substantially over the 1981–2024 period, most plausibly due to structural/technological factors rather than climate trends.
2. Both temperature and rainfall series are non-stationary in levels but become stationary after differencing.
3. After removing trend effects (via differencing), the relationship between climate variables and yield changes is weak:
 - Rainfall changes show a mild negative association with yield changes.
 - Temperature changes show a mild positive association with yield changes.
4. SARIMAX modeling on the differenced series supports rainfall as a modest, statistically significant predictor, while temperature's effect is not robust once trend and autocorrelation are properly accounted for.

## 10. Limitations & Next Steps

- Sample size is small (44 yearly observations), limiting statistical power.
- Only linear relationships were tested; nonlinear or lagged climate effects were not explored.
- Additional exogenous variables (e.g., soil quality, technology adoption, fertilizer use) could help isolate the true climate effect.
- Further model diagnostics (residual analysis, out-of-sample validation) would strengthen confidence in the SARIMAX results.
