# Time Series & Forecasting

Overview

This folder focuses on time series analysis and forecasting approaches relevant to agriculture: irrigation scheduling, yield forecasting, weather forecasting, and sensor monitoring.

What's included
- Notebooks with exploratory time series analysis, decomposition, feature engineering, classical models (ARIMA, SARIMA), Prophet, and modern approaches (LSTM, TCN, DeepAR).
- Evaluation examples with rolling-window validation and forecasting metrics.

Prerequisites
- Python 3.8+ and dependencies in the repository `requirements.txt`.

How to run
1. Install dependencies and prepare time series datasets in `data/`.
2. Make sure each notebook documents the timestamp column name and the frequency (hourly/daily/weekly).
3. Run notebooks; use sample data for quick experiments and full datasets for final results.

Best practices
- Always visualize the series, check for stationarity, and decompose into trend/seasonality/noise.
- Use time-based validation (no random shuffles) and evaluate with RMSE/MAE/MAPE depending on the use case.

Contributing
- When adding notebooks, include details about timestamp format, timezone handling, and any resampling performed.
- Provide scripts to reproduce preprocessing steps (missing value handling, interpolation, external regressors).