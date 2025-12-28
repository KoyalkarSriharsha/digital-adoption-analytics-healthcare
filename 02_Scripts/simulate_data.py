import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)

# 1. GENERATE PARTNER DIMENSION
partner_ids = [f'P{i:03d}' for i in range(1, 101)]
regions = ['Hyderabad', 'Secunderabad', 'Cyberabad', 'Outskirts']
types = ['Diagnostic Center', 'Home Care Agency']

partners = pd.DataFrame({
    'Partner_ID': partner_ids,
    'Partner_Name': [f'Partner_{i}' for i in range(1, 101)],
    'Region': np.random.choice(regions, 100),
    'Partner_Type': np.random.choice(types, 100, p=[0.7, 0.3]), # 70% DCs, 30% Home Care
    'Onboarding_Date': [datetime(2024, 1, 1) + timedelta(days=random.randint(0, 365)) for _ in range(100)]
})

# 2. GENERATE PORTAL LOGIN LOGS (Adoption Metric 1)
# Simulating that some partners log in frequently, others rarely
data_logs = []
for pid in partner_ids:
    # Assign a "tech savvy" score to each partner
    tech_score = random.random() 
    num_logins = int(np.random.poisson(10 * tech_score) * 4) # Weekly logins approx
    
    for _ in range(num_logins):
        data_logs.append({
            'Partner_ID': pid,
            'Login_Date': datetime(2025, 1, 1) + timedelta(days=random.randint(0, 90)),
            'Feature_Used': np.random.choice(['Dashboard', 'Reports', 'Payments', 'Profile'], p=[0.4, 0.3, 0.2, 0.1]),
            'Session_Duration_Mins': random.randint(2, 45)
        })

portal_logs = pd.DataFrame(data_logs)

# 3. GENERATE VISIT/UPLOAD TRANSACTIONS (Adoption Metric 2 & 3)
# Simulating adherence to Digital Uploads vs Manual
visit_data = []
for pid in partner_ids:
    num_visits = random.randint(10, 100) # Volume of business
    tech_score = random.random() # Re-rolling for variance in specific task adoption
    
    for _ in range(num_visits):
        is_app_used = np.random.choice([1, 0], p=[tech_score, 1-tech_score])
        report_upload_method = np.random.choice(['Digital_API', 'Manual_Email'], p=[tech_score, 1-tech_score])
        tat_hours = random.randint(4, 48) if report_upload_method == 'Digital_API' else random.randint(12, 72)
        
        visit_data.append({
            'Transaction_ID': f'TXN{random.randint(10000,99999)}',
            'Partner_ID': pid,
            'Date': datetime(2025, 1, 1) + timedelta(days=random.randint(0, 90)),
            'App_Used_For_Visit': is_app_used,
            'Report_Upload_Method': report_upload_method,
            'Turnaround_Time_Hours': tat_hours
        })

transactions = pd.DataFrame(visit_data)

# SAVE TO CSV (Use these for Power BI or SQL loading)
partners.to_csv('partners.csv', index=False)
portal_logs.to_csv('portal_logs.csv', index=False)
transactions.to_csv('transactions.csv', index=False)

print("Data Generated Successfully: partners.csv, portal_logs.csv, transactions.csv")