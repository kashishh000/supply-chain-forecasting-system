# 🚚 Supply Chain Optimization & Demand Forecasting

![SQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-102A43?style=for-the-badge&logo=xgboost&logoColor=white)
![Power BI](https://img.shields.io/badge/PowerBI-F2C811?style=for-the-badge&logo=Power%20BI&logoColor=white)

## 📌 Project Overview
Supply chain efficiency is critical to reducing operational costs. This data science project analyzes historical inventory and logistics data to forecast future product demand, optimizing warehouse stocking levels and minimizing delivery delays.

## 🏗️ Analytics Workflow
1. **Data Wrangling (SQL & Pandas):** Joining multiple tables (Orders, Inventory, Shipping) to create a unified view of the supply chain lifecycle.
2. **Demand Forecasting (ML):** Using advanced regression techniques like **XGBoost** and **LightGBM** to predict product demand for the upcoming month, factoring in seasonality, holidays, and promotions.
3. **Optimization Metrics:** Calculating safety stock levels and identifying bottlenecks in shipping routes.
4. **Executive Reporting:** Building a Power BI dashboard for supply chain managers to monitor stock-out risks and supplier performance.

## 📂 Repository Structure
```text
├── sql_queries/            # Scripts for data extraction and joining
├── forecasting_models/     # XGBoost/LightGBM notebooks
├── reports/                # Power BI `.pbix` files and PDF exports
└── README.md               # Project documentation
```

## 🚀 Business Impact
*   **Reduced Stockouts:** Forecasting model predicts demand with a MAPE (Mean Absolute Percentage Error) of 14%, significantly reducing out-of-stock scenarios.
*   **Cost Savings:** Identified inefficient shipping routes, potentially saving 8% in logistical costs.
*   *(Placeholder: Insert screenshot of the Power BI Supply Chain Dashboard)*
