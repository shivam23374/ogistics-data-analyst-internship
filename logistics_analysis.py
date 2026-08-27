"""
Week 1 - Logistics Data Analyst Internship
Strategic Planning and Data Exploration

This script demonstrates:
1. Data loading and validation
2. KPI calculation
3. Exploratory analysis
4. Delay prediction using logistic regression
"""

from pathlib import Path
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

DATA_PATH = Path("data/sample_logistics_orders.csv")

# 1. Load data
df = pd.read_csv(DATA_PATH, parse_dates=["order_date"])

# 2. Basic cleaning
df = df.drop_duplicates()
numeric_cols = [
    "distance_km", "weight_kg", "transport_cost",
    "delivery_time_hr", "expected_time_hr"
]
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")
df = df.dropna(subset=numeric_cols + ["transport_mode", "delayed"])

# 3. KPI calculation
on_time_rate = (1 - df["delayed"].mean()) * 100
avg_delivery_time = df["delivery_time_hr"].mean()
avg_transport_cost = df["transport_cost"].mean()
avg_cost_per_km = (df["transport_cost"] / df["distance_km"]).mean()
delay_rate = df["delayed"].mean() * 100

print(f"On-time delivery rate: {on_time_rate:.2f}%")
print(f"Average delivery time: {avg_delivery_time:.2f} hours")
print(f"Average transport cost: {avg_transport_cost:.2f}")
print(f"Average cost per km: {avg_cost_per_km:.4f}")
print(f"Delay rate: {delay_rate:.2f}%")

# 4. Mode-level exploration
mode_summary = df.groupby("transport_mode").agg(
    orders=("order_id", "count"),
    avg_delivery_hr=("delivery_time_hr", "mean"),
    delay_rate=("delayed", "mean"),
    avg_cost=("transport_cost", "mean")
).reset_index()

mode_summary["delay_rate"] *= 100
print("\nTransport-mode summary:")
print(mode_summary)

# 5. Predictive model for delivery delay
features = [
    "distance_km", "weight_kg", "transport_cost",
    "expected_time_hr", "transport_mode"
]
X = df[features]
y = df["delayed"]

numeric_features = [
    "distance_km", "weight_kg", "transport_cost", "expected_time_hr"
]
categorical_features = ["transport_mode"]

preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numeric_features),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
    ]
)

model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression(max_iter=1000))
])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

model.fit(X_train, y_train)
predictions = model.predict(X_test)

print("\nDelay prediction accuracy:",
      f"{accuracy_score(y_test, predictions):.2%}")
print(classification_report(y_test, predictions))

# 6. Business use:
# Use high-risk orders for proactive intervention,
# route/mode review, and resource allocation.
