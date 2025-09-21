# 📊 Automated Backup Reporting Dashboard (Power BI + GenAI)

## 📌 Overview
Designed a **Power BI dashboard** to monitor storage backup success, failure trends, and recovery performance.  
Added **GenAI-powered automated summaries** for quick executive insights.

---

## 🗂️ Dataset
- **File:** `backup_logs_sample.csv`  
- Contains mock backup logs with:
  - `JobID`
  - `Date`
  - `Status (Success/Failure)`
  - `Duration (mins)`
  - `Storage_Used (GB)`

---

## ⚙️ Steps
1. Import `backup_logs_sample.csv` into **Power BI**.  
2. Create KPIs:
   - Backup Success %  
   - Average Duration per Backup  
   - Failure Trend over Time  
3. Add filters (by date, status).  
4. Use **GenAI (e.g., ChatGPT, Copilot)** to auto-generate natural language summaries of key metrics.

---

## 🛠️ Tools
- Power BI  
- SQL (optional for preprocessing)  
- GenAI (for text summaries)  

---

## 📷 Sample Output
- Interactive dashboard with success/failure trend lines.  
- GenAI summary like:  
  *“Backup success rate was 95% last month, with 3 recurring failure patterns identified.”*
