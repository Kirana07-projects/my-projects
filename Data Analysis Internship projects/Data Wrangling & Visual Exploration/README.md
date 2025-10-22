# Week 02 — Sales & Customer Behaviour Insights (Green Card Ltd.)

**Goal:** Clean and consolidate three datasets (`sales_data`, `product_info`, `customer_info`) to analyse weekly revenue trends, product performance, loyalty behaviour, payments, and delivery reliability across regions and segments.

## Files in this folder
- [`Data Wrangling and Visual Exploration_week2.ipynb`](./Data%20Wrangling%20and%20Visual%20Exploration_week2.ipynb) — data wrangling, feature engineering, EDA, and charts  
- `Data Wrangling and Visual Exploration_week2.py` — Python export of the notebook  
- `Week 2 – Sales and Customer behaviour Insights – Kirana Dhinakar Raj.pdf` — full write-up  
- `datasets/` — CSV inputs used by the notebook (see **Data access**)

## Data access
- sales_data.csv
- customer_info.csv
- product_info.csv

## How to run

```bash
# from the repo root
cd "Data Analysis Internship projects/Data Wrangling & Visual Exploration"

# 1) Create & activate a virtual env
python -m venv .venv
# Windows PowerShell:
. .\.venv\Scripts\Activate.ps1
# macOS/Linux:
# source .venv/bin/activate

# 2) Upgrade pip and install deps
python -m pip install --upgrade pip
pip install -r requirements.txt   # create this file (see below)

# 3) Make Jupyter see this env (once)
python -m ipykernel install --user --name week2 --display-name "Python (week2)"

# 4) Launch Jupyter
jupyter lab .   # or: jupyter notebook



