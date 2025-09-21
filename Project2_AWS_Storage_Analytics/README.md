# ☁️ AWS Storage Utilization Analytics (Python + GenAI)

## 📌 Overview
Analyzed **AWS S3 + Glacier usage** to identify growth patterns, anomalies, and cost-saving opportunities.  
Used **Python (Pandas, Matplotlib)** for data analysis and **GenAI** for optimization recommendations.

---

## 🗂️ Dataset
- **File:** `storage_data_sample.csv`  
- Contains:
  - `Date`
  - `Bucket`
  - `Storage_Type (S3/Glacier)`
  - `Usage_GB`
  - `Cost_USD`

---

## ⚙️ Steps
1. Load data with `aws_storage_analysis.py`.  
2. Clean and preprocess with **Pandas**.  
3. Generate:
   - Storage growth trends  
   - Cost over time  
   - Forecasted usage  
4. Use GenAI to suggest:
   - Lifecycle rules (move infrequently accessed data to Glacier)  
   - Cost optimization actions  

---

## 🛠️ Tools
- Python (Pandas, Matplotlib)  
- AWS S3/Glacier (mock data)  
- GenAI  

---

## 📷 Sample Output
- Line chart: Storage usage growth  
- Bar chart: Monthly costs  
- GenAI recommendation:  
  *“Move 20% of rarely accessed objects to Glacier to save ~$500/month.”*
