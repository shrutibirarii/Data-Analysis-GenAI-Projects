Automated Backup Reporting Dashboard (Power BI + GenAI)

Files included:
- backup_logs_sample.csv : sample backup log dataset

How to build the dashboard (quick steps):
1. Open Power BI Desktop.
2. Get Data -> CSV -> select 'backup_logs_sample.csv'.
3. In Power Query: parse 'timestamp' to Date/Time, create Date/Hour/Month columns.
4. Create visuals: KPI cards (Total Backups, Success Rate), Line chart for trends, Bar chart for failures by server.
5. To add AI summaries: copy KPIs and ask a GenAI model to summarize (example prompt in README).
