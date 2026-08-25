# Time Series Analysis: Crop Yield vs Climate

A time series analysis exploring the relationship between crop yield, average temperature, and annual rainfall using historical data (1981–2024).

## Project Structure

```
.
├── README.md
├── report.md              # (to be added)
├── data/                   # (to be added) contains time_series_data.csv
└── Time_Series_Analysis.ipynb
```

## Dataset

The dataset (`time_series_data.csv`) contains yearly records with the following columns:

| Column | Description |
|---|---|
| `year` | Year of observation |
| `yield_kg_ha` | Crop yield (kg/ha) |
| `avg_temp_c` | Average temperature (°C) |
| `annual_rainfall_mm` | Annual rainfall (mm) |

## Analysis Overview

1. **Data Import & Visualization** — Loaded the dataset and plotted crop yield, temperature, and rainfall over time.
2. **Time Trend** — Added an explicit time index (`time`) to capture the overall trend.
3. **First Differencing** — Computed year-over-year changes (`yield_change`, `temp_change`, `rainfall_change`) to remove trend and examine short-term relationships.
4. **Correlation Analysis** — Checked correlation between changes in temperature/rainfall and changes in yield.
5. **Stationarity Testing (ADF Test)** — Verified that raw series were non-stationary, while differenced series were stationary (p < 0.05).
6. **Autocorrelation (ACF)** — Examined how crop yield in a given year relates to previous years.
7. **Climate Relationships** — Visualized yield vs. temperature and yield vs. rainfall, both in raw and differenced (change) form.
8. **SARIMAX Modeling** — Fit SARIMAX models using temperature and rainfall as exogenous variables to predict crop yield, comparing different `(p,d,q)` orders and trend specifications.

## Requirements

```
pandas
numpy
matplotlib
seaborn
statsmodels
```

## Usage

1. Place `time_series_data.csv` inside the `data/` folder.
2. Update the file path in the notebook to point to `data/time_series_data.csv`.
3. Run the notebook cells in order.

## Notes

- See `report.md` for detailed findings and interpretation (to be added).
