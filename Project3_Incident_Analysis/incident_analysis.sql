-- incident_analysis.sql
-- Queries for incident_logs loaded into a SQL table 'incidents'
SELECT incident_type, COUNT(*) AS frequency
FROM incidents
GROUP BY incident_type
ORDER BY frequency DESC;

SELECT system, COUNT(*) AS failure_count
FROM incidents
WHERE status = 'Failure'
GROUP BY system
HAVING COUNT(*) > 5
ORDER BY failure_count DESC;

-- Monthly trend (SQLite syntax)
SELECT strftime('%Y-%m', date) AS month, COUNT(*) AS incidents
FROM incidents
GROUP BY month
ORDER BY month;
