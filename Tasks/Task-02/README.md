# Task 02 – From Tables to Notebooks

## Overview

This task builds an end-to-end machine learning workflow using the Olist dataset, starting from PostgreSQL tables and ending with a trained and evaluated classification model.

The goal is to predict whether an order will be delivered **Late** or **On-time**.

## Notebooks

The workflow is organized into six notebooks:

1. `01_read_join.ipynb`
   - Reads the Olist tables from PostgreSQL.
   - Checks duplicates and key uniqueness.
   - Aggregates order items and payments.
   - Creates the order-level machine learning table.

2. `02_create_labels.ipynb`
   - Creates the target label.
   - Orders delivered after the estimated delivery date are labeled `Late`.
   - Other eligible orders are labeled `On-time`.

3. `03_train_val_test_split.ipynb`
   - Performs a chronological train/validation/test split.
   - Uses approximately 70% training, 15% validation, and 15% testing data.

4. `04_eda.ipynb`
   - Performs exploratory data analysis on the training data.
   - Examines missing values, distributions, correlations, categorical variables, and target imbalance.

5. `05_feature_engineering.ipynb`
   - Creates time-based and delivery-window features.
   - Applies numerical and categorical preprocessing.
   - Fits preprocessing only on training data to avoid data leakage.

6. `06_train_tune_evaluate.ipynb`
   - Creates a DummyClassifier baseline.
   - Trains Logistic Regression.
   - Tunes the model using validation data.
   - Performs final evaluation on the test set.

## Model

The final model is a Logistic Regression classifier with class balancing.

Best validation hyperparameter:

- `C = 0.1`

Final test results:

- Accuracy: 0.4835
- Precision: 0.0993
- Recall: 0.8443
- F1 Score: 0.1778
- ROC-AUC: 0.6705

The high recall indicates that the model identifies a large proportion of late deliveries, although this comes with a relatively high number of false positives.

## Project Structure

```text
Task-02/
├── notebooks/
│   ├── 01_read_join.ipynb
│   ├── 02_create_labels.ipynb
│   ├── 03_train_val_test_split.ipynb
│   ├── 04_eda.ipynb
│   ├── 05_feature_engineering.ipynb
│   └── 06_train_tune_evaluate.ipynb
│
├── artifacts/
│   ├── eda_charts/
│   ├── feature_list.txt
│   ├── logistic_regression_model.joblib
│   ├── model_results_summary.csv
│   └── preprocessor.joblib
│
└── README.md