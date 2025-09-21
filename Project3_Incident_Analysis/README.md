# 🚨 Incident Analysis & AI-Enhanced Root Cause Reports

## 📌 Overview
Queried **incident logs** using SQL to identify recurring issues and failure clusters.  
Automated **root cause summaries** using GenAI to speed up report writing.

---

## 🗂️ Dataset
- **File:** `incident_logs.csv`  
- Fields:
  - `IncidentID`
  - `Date`
  - `Category`
  - `Severity`
  - `Resolution_Time (hrs)`
  - `Root_Cause`

---

## ⚙️ Steps
1. Import `incident_logs.csv` into a SQL database.  
2. Run queries from `incident_analysis.sql`:
   - Most common failure categories  
   - Average resolution times  
   - High severity incident patterns  
3. Feed query results into GenAI for **natural language RCA reports**.  

---

## 🛠️ Tools
- SQL (MySQL/Postgres/SQLite)  
- Excel (for quick pivot tables)  
- GenAI  

---

## 📷 Sample Output
- Query result: Top 3 categories causing downtime.  
- GenAI summary:  
  *“80% of downtime in Q1 was caused by recurring network errors and misconfigured backup jobs.”*

