# Week 01 — Customer Sign-Up Behaviour & Data Quality Audit

**Goal:** Analyze customer sign-up patterns and perform a data-quality audit for a SaaS product with tiered plans. Results are intended for Marketing and Onboarding stakeholders.

---

## Dataset
- **Source file:** `customer_signups.csv` (provided for the exercise)  
- **Shape:** 300 rows × 10 columns  
- **Columns:** `customer_id`, `name`, `email`, `signup_date`, `source`, `region`, `plan_selected`, `marketing_opt_in`, `age`, `gender`  
- **Notes:** Raw data contained missing values, inconsistent categories (e.g., case/typo variants), and invalid dates (e.g., `"not a date"`).

## Files in this folder
- `customer_signups_Week1_task.ipynb` — code used for cleaning, EDA, and aggregations  
- `Week 1 – Customer Sign-Up Behaviour & Data Quality Audit - Kirana Dhinakar Raj.pdf` — full write-up of this week’s work
- 'datasets/' - CSV files used for this task

---

## How to run
```bash
# create & activate a virtual env (macOS/Linux)
python -m venv .venv && source .venv/bin/activate
# on Windows: .venv\Scripts\activate

# install essentials
pip install pandas numpy jupyter

# open the notebook
jupyter notebook "customer_signups_Week1_task.ipynb"

