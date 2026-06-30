# 🌧️ Rainfall Forecasting using Machine Learning

A complete end-to-end machine learning pipeline for predicting whether it will rain tomorrow using historical weather data.

This project covers the entire workflow from data preprocessing to model evaluation, making it suitable for beginners learning classification problems in Python.

---

## 📌 Project Overview

The objective of this project is to predict the **RainTomorrow** variable using weather observations.

The notebook includes:

- Data loading
- Data cleaning
- Missing value handling
- Feature encoding
- Train-test split
- Class imbalance handling using SMOTE and `class_weight='balanced'`
- Model training
- Prediction
- Performance evaluation
- ROC Curve visualization

---

## 📂 Dataset

The project uses a weather dataset (`weather.csv`) containing meteorological observations.

Example features include:

- Date
- Location
- Temperature
- Rainfall
- Humidity
- Pressure
- Wind Speed
- Wind Direction
- Cloud Cover
- Sunshine
- Evaporation

Target Variable:

- **RainTomorrow**
  - Yes
  - No

---

# 🛠 Libraries Used

```python
pandas
numpy
matplotlib
seaborn
scikit-learn
```

---

# 📊 Workflow

## 1. Import Libraries

- Pandas
- NumPy
- Matplotlib
- Seaborn

---

## 2. Load Dataset

Read the weather dataset into a Pandas DataFrame.

---

## 3. Data Cleaning

### Missing Value Visualization

A heatmap is used to identify missing values.

---

### Drop Columns

Columns having more than **35% missing values** are removed.

Example:

- Evaporation
- Sunshine
- Cloud9am
- Cloud3pm

---

### Remove Missing Target

Rows where **RainTomorrow** is missing are removed.

---

### Fill Missing Values

Numerical columns

- Filled using Median

Categorical columns

- Filled using Mode

---

## 4. Encode Categorical Variables

Convert categorical columns into numerical values using Label Encoding.

Examples:

- Yes → 1
- No → 0

---

## 5. Split Dataset

Separate:

- Features (X)
- Target (y)

Perform train-test split.

Typical split:

- 80% Training
- 20% Testing

---

## 6. Handle Class Imbalance

The target variable (**RainTomorrow**) was imbalanced, meaning one class had significantly more samples than the other. To improve the model's ability to correctly identify the minority class, two complementary techniques were applied.

### SMOTE (Synthetic Minority Over-sampling Technique)

SMOTE was used **only on the training dataset** to generate synthetic samples for the minority class. This helps balance the class distribution without simply duplicating existing observations.

**Benefits:**

- Reduces class imbalance
- Improves minority class prediction
- Helps prevent model bias toward the majority class

---

### Algorithmic Balancing

In addition to SMOTE, the model was trained using:

```python
class_weight='balanced'
```

This automatically assigns higher weights to the minority class during training, causing misclassification of minority samples to incur a larger penalty.

**Benefits:**

- Handles residual class imbalance
- Improves Recall and F1-score
- Reduces bias toward the majority class

---

### Why Both Techniques?

This project combines **data-level balancing (SMOTE)** with **algorithm-level balancing (`class_weight='balanced'`)**.

- **SMOTE** creates synthetic minority samples.
- **`class_weight='balanced'`** adjusts the learning algorithm to give more importance to minority-class predictions.

Using both techniques often leads to a more robust classifier, particularly when predicting rare events such as rainfall.

---

## 7. Model Training

The notebook trains a machine learning classification model for rainfall prediction.

---

## 8. Prediction

Generate predictions on the test dataset.

---

## 9. Model Evaluation

Performance is evaluated using:

- Accuracy Score
- Confusion Matrix
- Classification Report

---

## 10. ROC Curve

The notebook computes:

- False Positive Rate (FPR)
- True Positive Rate (TPR)
- Area Under Curve (AUC)

and visualizes the ROC Curve.

---

# 📈 Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC
- Confusion Matrix

---


# 🚀 How to Run

## Clone Repository

```bash
git clone https://github.com/yourusername/rainfall-forecasting.git
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Open Notebook

```bash
jupyter notebook
```

or

Open directly in Google Colab.

---

# 📦 Requirements

```
pandas
numpy
matplotlib
seaborn
scikit-learn
```

---

# 🎯 Learning Outcomes

After completing this project, you will understand:

- Data preprocessing
- Missing value handling
- Feature encoding
- Classification workflow
- Model training
- Model evaluation
- ROC Curve analysis
- Binary classification using Scikit-learn
- Handling imbalanced datasets
- Applying SMOTE for oversampling
- Using `class_weight='balanced'` in classification models
- Evaluating models trained on balanced data

---

# 📚 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
- Google Colab

---

# 📜 License

This project is intended for educational and learning purposes.

---
