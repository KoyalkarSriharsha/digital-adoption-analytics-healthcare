# Digital Adoption Analytics – Healthcare Partner Ecosystem

### 📌 Project Overview
**Goal:** Improve operational efficiency and digital adoption across a healthcare partner ecosystem (Diagnostic Centers & Home Care Agencies). 
**Context:** The business relies on partners adopting digital tools (Portals, APIs) to reduce Turnaround Time (TAT) and improve network quality. This simulated project analyzes adoption gaps and segments partners for strategic intervention.

---

### 🛠️ Tech Stack
* **Python:** Pandas, NumPy (Data Generation, Cleaning, Segmentation Analysis)
* **SQL:** Data Engineering (Creating a "Partner 360" View)
* **DuckDB:** Local SQL analytics engine
* **Power BI:** Dynamic Dashboards for Executive Reporting

---

### 📊 Key Insights Generated
1.  **Impact on Efficiency:** Digital API adoption correlates with a **~40% reduction in Turnaround Time (TAT)** for report delivery.
2.  **Adoption Gaps:** The "Outskirts" region has the highest volume of manual uploads (65%), indicating a need for targeted training.
3.  **Risk Segmentation:** Identified **High-Volume Partners** who are "Digital Laggards," representing a critical bottleneck in the ecosystem.

---

### 📂 Repository Structure
* `01_Data/`: Synthetic datasets generated to mimic partner logs and interactions.
* `02_Scripts/`: Python logic for data simulation and statistical analysis.
* `03_SQL/`: SQL queries used to aggregate partner performance metrics.
* `04_Dashboard/`: Power BI file (exported in pdf format) containing the executive view.

---

### 🚀 How to Use
1.  Run `02_Scripts/simulate_data.py` to create the dataset.
2.  Execute `03_SQL/run_query.py` to build the analytical dataset.
3.  Open `04_Dashboard/` to view dashboard for interactive insights (in pdf format).

---
*Author: Koyalkar Sri Harsha* 

*LinkedIn: [www.linkedin.com/in/koyalkar-sri-harsha]*
