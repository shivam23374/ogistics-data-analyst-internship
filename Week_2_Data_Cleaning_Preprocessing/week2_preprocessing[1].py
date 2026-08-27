"""
Week 2 - Data Collection, Cleaning, and Preprocessing
Logistics Data Analyst Internship

Input : sample_logistics_orders.csv
Output: cleaned_logistics_orders.csv
"""

import pandas as pd

INPUT_FILE = "sample_logistics_orders.csv"
OUTPUT_FILE = "cleaned_logistics_orders.csv"

NUMERIC_COLS = [
    "Distance_km",
    "Weight_kg",
    "Expected_Delivery_Hours",
    "Actual_Delivery_Hours",
    "Transport_Cost",
]


def iqr_outlier_mask(series: pd.Series) -> pd.Series:
    """Return True for observations outside the 1.5 x IQR limits."""
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    return (series < lower) | (series > upper)


def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = df.columns.str.strip()

    # Convert numeric columns safely.
    for col in NUMERIC_COLS:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Standardize categorical values.
    df["Transport_Mode"] = (
        df["Transport_Mode"].astype("string").str.strip().str.title()
    )

    # Business-rule validation: distance cannot be negative/zero.
    df.loc[df["Distance_km"] <= 0, "Distance_km"] = pd.NA

    # Remove duplicate shipment records using the shipment ID.
    df = df.drop_duplicates(subset=["Shipment_ID"], keep="first").reset_index(drop=True)

    # Median imputation for numeric missing values.
    for col in NUMERIC_COLS:
        df[col] = df[col].fillna(df[col].median())

    # Controlled category for missing transport mode.
    df["Transport_Mode"] = df["Transport_Mode"].fillna("Unknown")

    # Flag, rather than automatically delete, IQR outliers.
    for col in NUMERIC_COLS:
        df[col + "_outlier"] = iqr_outlier_mask(df[col]).astype(int)

    # Derived logistics metrics.
    df["Delay_Hours"] = (
        df["Actual_Delivery_Hours"] - df["Expected_Delivery_Hours"]
    ).round(2)
    df["On_Time"] = (df["Delay_Hours"] <= 0).astype(int)
    df["Cost_per_km"] = (
        df["Transport_Cost"] / df["Distance_km"]
    ).round(2)

    return df


def main():
    df = pd.read_csv(INPUT_FILE)
    cleaned = preprocess(df)
    cleaned.to_csv(OUTPUT_FILE, index=False)

    print(f"Input rows : {len(df)}")
    print(f"Output rows: {len(cleaned)}")
    print(f"Saved to   : {OUTPUT_FILE}")
    print("\nMissing values after preprocessing:")
    print(cleaned.isna().sum())


if __name__ == "__main__":
    main()
