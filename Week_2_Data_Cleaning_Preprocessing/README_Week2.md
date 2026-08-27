# Week 2 — Data Collection, Cleaning & Preprocessing

## Objective
This project demonstrates a reproducible data-preprocessing pipeline for a logistics analytics scenario. Shipment records are inspected, cleaned, validated, and transformed into an analysis-ready dataset.

## Files
- `sample_logistics_orders.csv` — synthetic raw shipment data containing realistic data-quality issues.
- `cleaned_logistics_orders.csv` — processed output.
- `week2_preprocessing.py` — Python preprocessing pipeline.
- `requirements.txt` — Python dependency.
- `README_Week2.md` — project documentation.

## Workflow
**Raw Data → Inspection → Cleaning → Missing Values → Outlier Detection → Feature Engineering → Validation → Clean Dataset**

### Cleaning performed
1. Standardized column names and transport-mode labels.
2. Converted numerical fields to numeric types.
3. Flagged invalid non-positive distance and handled it as missing.
4. Removed duplicate shipment IDs.
5. Filled appropriate numerical missing values using medians.
6. Filled missing transport mode with `Unknown`.
7. Flagged numerical outliers using the 1.5 × IQR rule.
8. Created `Delay_Hours`, `On_Time`, and `Cost_per_km` features.

## Important methodology note
Outliers are **flagged rather than automatically removed**, because an extreme shipment may be operationally valid. In a production environment, treatment should be based on business rules and stakeholder review.

For machine-learning workflows, preprocessing parameters such as imputation values and scalers should be learned from the training set only to prevent data leakage.

## Run locally

```bash
pip install -r requirements.txt
python week2_preprocessing.py
```

The script reads `sample_logistics_orders.csv` and creates/updates `cleaned_logistics_orders.csv`.

## Dataset
The dataset is synthetic and intended for internship demonstration and reproducibility. It does not contain confidential operational data.

## Future Improvements
- Connect approved real logistics data sources.
- Add automated data-quality tests.
- Add visual EDA and KPI dashboards.
- Build a delay-risk classification model.
- Add route and transport-mode optimization.
