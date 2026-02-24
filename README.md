# Fuel Consumption Prediction for Construction Machinery (Diesel Engines)

## 1. Problem Statement

### Objective

This project aims to predict **ton-kilometer fuel consumption (L/km/t)** for heavy-duty construction and mining trucks operating in open-pit coal mines.

The prediction model considers:

* Vehicle specifications
* Engine displacement and power
* Load capacity
* Environmental conditions
* Terrain characteristics
* Seasonal effects

### Why This Matters

Fuel represents a major operating cost in mining and construction fleets. Accurate prediction of fuel consumption enables:

* Better **fleet cost forecasting**
* Improved **Ton/km/L efficiency analysis**
* Seasonal cost impact assessment
* Data-driven vehicle selection for specific applications
* Enhanced fleet return on investment (ROI)

### Beneficiaries

* Fleet managers
* Mining operators
* OEM performance analysts
* Heavy equipment simulation engineers

---

## 2. Dataset

### Source

Real-time operational dataset from unmanned mining trucks:

**Figshare Dataset:**
*A Dataset for Fuel Consumption Prediction in Driverless Mining Trucks Using Deep Siamese Transformer Networks*

(292 operational records)

---

### Target Variable

**Ton-kilometer fuel consumption (L/km/t)**
Fuel used per ton of material transported per kilometer.

---

### Core Operational Features

| Category      | Features                                                  |
| ------------- | --------------------------------------------------------- |
| Environmental | Average temperature, wind speed, precipitation            |
| Terrain       | Road quality, raise height difference, working flat width |
| Operational   | Mileage, fueling quantity, shift work                     |
| Temporal      | Date (used for seasonal modeling)                         |

---

### Engine & Vehicle Specification Augmentation

To improve scalability and engineering interpretability, the dataset was extended with engine specifications:

| Vehicle Model       | RTH136        | MT96         | SKT105E      |
| ------------------- | ------------- | ------------ | ------------ |
| Engine Model        | YCK16775-T300 | WP13G530E310 | WP13G530E310 |
| Engine Power (HP)   | 764           | 523          | 523          |
| Engine Size (L)     | 15.93         | 12.54        | 12.54        |
| Vehicle Weight (kg) | 48000         | 33000        | 38000        |
| Transmission        | Automatic     | Automatic    | Automatic    |
| Cylinders           | 6             | 6            | 6            |
| Load Capacity (kg)  | 100000        | 65000        | 70000        |

This allowed the model to incorporate:

* Power-to-weight relationships
* Displacement impact on fuel burn
* Load-based fuel scaling

---

### Dataset Overview

* Total Samples: 292
* Numerical Features: 16
* Categorical Features: 3
* Date Feature: 1

Missing values were present in:

* Mileage (km)
* Actual fueling quantity (L)

---

## 3. Methodology

### 3.1 Data Construction

* Merged operational dataset with engine specifications
* Standardized units
* Verified consistency across vehicle models

---

### 3.2 Exploratory Data Analysis (EDA)

#### Basic EDA

* Shape and datatype inspection
* Null value assessment

#### Deep EDA

* Histograms for distribution analysis
* Box plots for outlier detection
* Correlation heatmap for feature relationships
* Categorical feature impact analysis

---

### 3.3 Feature Engineering

* Extracted cyclic temporal components from date
* One-hot encoding for categorical variables
* Load-to-power interaction features
* Terrain elevation impact modeling

---

### 3.4 Data Preparation

* Train-test split
* Iterative Imputer for missing values
* RobustScaler for numerical scaling

---

### 3.5 Models Implemented

1. **RidgeCV Regression** (baseline regularized linear model)
2. **Random Forest Regressor**
3. **XGBoost Regressor**

---

## 4. Model Configurations

### Ridge Regression

Alpha optimized using cross-validation (RidgeCV).

---

### Random Forest

```python
RandomForestRegressor(
    n_estimators=300,
    max_depth=8,
    min_samples_split=5,
    random_state=42
)
```

---

### XGBoost

```python
XGBRegressor(
    n_estimators=300,
    learning_rate=0.05,
    max_depth=4,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42
)
```

---

## 5. Installation

```bash
git clone https://github.com/your-username/fuel-consumption-prediction.git
cd fuel-consumption-prediction
pip install -r requirements.txt
```

---

## 6. Usage

Train the model:

```bash
python train.py
```

Run prediction:

```bash
python predict.py --input sample_data.csv
```

---

## 7. Results

| Model         | Train R²  | Test R²   |
| ------------- | --------- | --------- |
| Ridge         | 0.854     | 0.766     |
| Random Forest | **0.961** | **0.896** |
| XGBoost       | 0.985     | 0.842     |

### Key Observations

* Random Forest achieved the best generalization performance.
* XGBoost showed signs of mild overfitting.
* Ridge regression underperformed due to nonlinear feature interactions.

The Random Forest model achieved:

* **Test R² = 0.896**
* Strong stability between train and test datasets
* Good interpretability through feature importance

---

## 8. Evaluation Metrics

Metrics used:

* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* Mean Absolute Error (MAE)
* R² Score
* Explained Variance

The evaluation framework was modularized for reproducibility.

---

## 9. Project Structure

```
├── data/
├── notebooks/
├── src/
│   ├── preprocessing.py
│   ├── train.py
│   ├── evaluate.py
│   └── utils.py
├── models/
├── requirements.txt
└── README.md
```

---

## 10. Future Improvements

* Increase dataset size for better generalization
* Integrate physics-informed features (BSFC maps)
* Add SHAP-based explainability
* Deploy as REST API (FastAPI)
* Integrate real-time telemetry prediction

---

## 11. Author

**Anish Nilesh Rane**
Mechanical Engineer | Machine Learning Engineer
Specializing in Powertrain Systems, Thermal Modeling & Applied ML

---

# 12. Feature Importance & Model Interpretability

Understanding *why* the model predicts a certain fuel consumption value is critical for engineering deployment.

### Random Forest Feature Importance

The most influential features identified were:

* Raise height difference (terrain elevation impact)
* Load Capacity
* Engine Power (HP)
* Vehicle Weight
* Road Quality
* Ambient Temperature

### Engineering Interpretation

* **Raise height difference** directly affects required tractive effort → increases fuel burn.
* **Load capacity + vehicle weight** influence rolling resistance and engine load.
* **Engine power-to-weight ratio** affects operating efficiency zone.
* **Environmental conditions** impact combustion efficiency and air density.

This confirms that the model is learning physically meaningful relationships rather than random correlations.

---

# 13. Physics-Informed Insight

Although this project uses purely data-driven ML models, several features align with first-principle mechanics:

### 13.1 Tractive Power Relationship

Fuel consumption in haul trucks is primarily influenced by:

[
P = F \cdot v
]

Where:

* ( F ) = Rolling resistance + Grade resistance
* ( v ) = Velocity

Grade resistance depends on elevation change:

[
F_{grade} = m g \sin(\theta)
]

The feature **Raise height difference** acts as a proxy for grade angle ( \theta ).

---

### 13.2 Load Impact

Fuel burn scales approximately with engine load:

[
\text{Fuel Rate} \propto \frac{\text{Brake Power}}{\eta_{thermal}}
]

Higher payload → higher required brake power → increased fuel consumption.

The model indirectly captures this via:

* Load Capacity
* Vehicle Weight
* Engine Power

---

### 13.3 Seasonal & Environmental Effects

Ambient temperature affects:

* Air density
* Combustion efficiency
* Rolling resistance (road conditions)

Wind speed influences aerodynamic drag:

[
F_d = \frac{1}{2} \rho C_d A v^2
]

The inclusion of temperature and wind variables improves seasonal robustness.

---

# 14. Model Validation Strategy

To ensure robustness:

* Train-test split performed with random_state=42
* Overfitting monitored via train vs test R² gap
* Cross-validation used in RidgeCV
* Hyperparameters tuned conservatively

### Overfitting Check

| Model | Train R² | Test R² | Gap   |
| ----- | -------- | ------- | ----- |
| RF    | 0.961    | 0.896   | 0.065 |
| XGB   | 0.985    | 0.842   | 0.143 |

The smaller generalization gap in Random Forest indicates better real-world stability.

---

# 15. Business Impact Estimation

Assume:

* Fleet size: 50 trucks
* Annual fuel consumption per truck: ~300,000 L
* Diesel cost: ₹90/L

Total annual fuel cost ≈ ₹1.35 billion

Even a **3% prediction-driven optimization improvement** could yield:

[
₹40+ million annual savings
]

This demonstrates real financial relevance of accurate modeling.

---

# 16. Deployment Considerations

For production use:

* Convert model to serialized `.pkl`
* Build FastAPI endpoint
* Integrate with fleet telematics API
* Enable real-time prediction dashboard

Future scope includes:

* Live telemetry ingestion
* Predictive maintenance integration
* Engine efficiency zone mapping

---

# 17. Limitations

* Small dataset (292 samples)
* Limited diversity of engine models
* No real-time RPM or torque sensor data
* Does not directly incorporate BSFC maps

These constraints define next research direction.

---

# 18. Research Extension Path

To elevate this into a publishable-grade system:

* Integrate BSFC contour maps
* Add torque and RPM sensor data
* Implement hybrid Physics + ML model
* Use SHAP for explainability
* Apply time-series cross-validation
* Expand dataset across multiple mine sites

---
