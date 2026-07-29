# 🌾 Crop Yield Prediction

A machine learning project that predicts cereal yield (t/ha) based on fertilizer use, rainfall, and temperature, using country-level agricultural data from 1961–2023.

## 📌 Overview

This project explores the relationship between cereal yield and key environmental/agricultural factors, then builds and compares three regression models to predict yield:

- **Linear Regression** (baseline)
- **Decision Tree Regression**
- **Random Forest Regression**

## 📊 Dataset

The dataset (`Yield.csv`) contains 9,168 rows across multiple countries and years (1961–2023), with the following columns:

| Column            | Description                          |
|--------------------|---------------------------------------|
| `Entity`           | Country name                          |
| `Code`             | Country code (ISO)                    |
| `Year`             | Year of observation                    |
| `yield_t_ha`       | Cereal yield (tonnes per hectare)      |
| `fertilizer_kg_ha` | Fertilizer use (kg per hectare)        |
| `rainfall_mm`      | Annual rainfall (mm)                   |
| `temperature_c`    | Average annual temperature (°C)        |

## 🔍 Exploratory Data Analysis

- Scatter plots of yield vs. fertilizer use, rainfall, and temperature
- Correlation matrix between yield and the three predictor variables

**Key findings:**
- Fertilizer use shows a moderate positive correlation with yield (**0.45**)
- Rainfall shows almost no linear correlation with yield (**-0.005**)
- Temperature shows a weak negative correlation with yield (**-0.23**)

## 🧠 Models & Results

| Model             | MAE  | RMSE | R²   |
|-------------------|------|------|------|
| Linear Regression | 1.22 | 2.22 | 0.22 |
| Decision Tree      | 1.00 | 1.85 | 0.46 |
| Random Forest      | 0.80 | 1.63 | 0.58 |

The **Random Forest Regressor** performed best, explaining ~58% of the variance in yield, a notable improvement over the linear baseline.

### Model Configurations

**Decision Tree**
```python
DecisionTreeRegressor(max_depth=3, min_samples_leaf=50, random_state=42)
```

**Random Forest**
```python
RandomForestRegressor(n_estimators=500, max_depth=10, min_samples_leaf=30, random_state=42, n_jobs=-1)
```

## 🛠️ Tech Stack

- Python
- pandas, numpy
- matplotlib, seaborn
- scikit-learn
- statsmodels

## 📁 Project Structure

```
yield-prediction/
├── data/
│   └── Yield.csv
├── Yield_Prediction.ipynb
├── README.md
└── requirements.txt
```

## 🚀 Getting Started

1. Clone the repository
   ```bash
   git clone https://github.com/<your-username>/yield-prediction.git
   cd yield-prediction
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Open and run the notebook
   ```bash
   jupyter notebook Yield_Prediction.ipynb
   ```

   > Note: Update the CSV file path in the notebook to `data/Yield.csv` (the original path in the notebook points to a Google Drive location).

## 📈 Future Improvements

- Add more features (soil type, pesticide use, irrigation)
- Try gradient boosting models (XGBoost, LightGBM)
- Hyperparameter tuning with GridSearchCV / RandomizedSearchCV
- Handle outliers (some yield values >20 t/ha appear to be extreme outliers)

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
