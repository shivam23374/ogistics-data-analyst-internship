# Logistics Data Analyst Internship — Week 1

## Project
**Strategic Planning and Data Exploration in Logistics**

This repository contains the Week 1 deliverables for a logistics data-analysis project focused on improving delivery reliability, transport cost visibility, and resource allocation.

## Business Scenario
A logistics company wants to reduce delivery delays while controlling transportation cost. The analysis evaluates order-level distance, shipment weight, transport mode, delivery time, expected delivery time, and transport cost.

## KPIs
- On-Time Delivery Rate
- Delivery Delay Rate
- Average Delivery Time
- Average Transport Cost
- Average Transport Cost per Kilometer

## Data
The repository includes a clearly labelled **synthetic sample dataset** for demonstration. The proposed production analysis can be extended using public freight-flow data such as the U.S. Department of Transportation Freight Analysis Framework (FAF6).

## Workflow
Data Collection → Data Cleaning → Exploratory Data Analysis → KPI Analysis → Delay Prediction → Operational Decision

## Repository Structure
```text
logistics_data_analyst_week1/
├── data/
│   └── sample_logistics_orders.csv
├── docs/
│   └── Week_1_Strategic_Planning_Logistics.docx
├── src/
│   └── logistics_analysis.py
├── requirements.txt
└── README.md
```

## Run
```bash
pip install -r requirements.txt
python src/logistics_analysis.py
```

## Expected Business Value
The approach helps logistics teams identify delay-risk orders, compare transport modes, monitor service levels, and prioritize operational interventions.

## Data Source Note
For a real implementation, FAF6 provides public freight-flow estimates by origin, destination, commodity, and mode. See the official BTS documentation for details.
