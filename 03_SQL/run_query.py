import duckdb

# Optional: set working directory if CSVs are elsewhere
# import os
# os.chdir(r"C:\path\to\csvs")

query = """
WITH Portal_Stats AS (
    SELECT 
        Partner_ID, 
        COUNT(*) AS Total_Logins,
        AVG(Session_Duration_Mins) AS Avg_Session_Time,
        COUNT(DISTINCT Feature_Used) AS Features_Explored
    FROM read_csv_auto('portal_logs.csv')
    GROUP BY Partner_ID
),
Transaction_Stats AS (
    SELECT 
        Partner_ID,
        COUNT(*) AS Total_Volume,
        SUM(App_Used_For_Visit) * 1.0 / COUNT(*) AS App_Adoption_Rate,
        SUM(CASE WHEN Report_Upload_Method = 'Digital_API' THEN 1 ELSE 0 END) * 1.0 / COUNT(*) AS Digital_Upload_Rate,
        AVG(Turnaround_Time_Hours) AS Avg_TAT
    FROM read_csv_auto('transactions.csv')
    GROUP BY Partner_ID
)
SELECT 
    p.Partner_ID,
    p.Partner_Name,
    p.Partner_Type,
    p.Region,
    COALESCE(ps.Total_Logins, 0) AS Portal_Logins,
    COALESCE(ts.App_Adoption_Rate, 0) AS Home_Visit_App_Usage,
    COALESCE(ts.Digital_Upload_Rate, 0) AS Report_Digital_Upload_Usage,
    COALESCE(ts.Avg_TAT, 0) AS Avg_Turnaround_Time,
    CASE 
        WHEN COALESCE(ts.Digital_Upload_Rate, 0) > 0.8 AND COALESCE(ps.Total_Logins, 0) > 10 THEN 'High Adopter'
        WHEN COALESCE(ts.Digital_Upload_Rate, 0) > 0.4 THEN 'Developing'
        ELSE 'Laggard'
    END AS Digital_Maturity_Segment
FROM read_csv_auto('partners.csv') AS p
LEFT JOIN Portal_Stats ps ON p.Partner_ID = ps.Partner_ID
LEFT JOIN Transaction_Stats ts ON p.Partner_ID = ts.Partner_ID
"""

# Execute and fetch to a DataFrame
df = duckdb.sql(query).df()
print(df.head())

# Optional: write results to CSV
duckdb.execute(f"COPY ({query}) TO 'digital_maturity_scores.csv' WITH (FORMAT CSV, HEADER TRUE);")
print("Results saved to digital_maturity_scores.csv")