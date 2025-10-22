# Week 04 — Dashboards & AI

**Goal:** Explore and communicate KPIs using notebooks + Tableau dashboards. All inputs (notebooks, datasets, Tableau workbook) are packaged in `project files.zip`. The PDF contains the online Tableau link.

## Files in this folder
- `project files.zip` — notebooks, datasets, Tableau workbook
- `Week4-Project Brief-Dashboards & AI.pdf` — project brief (includes Tableau link)

## How to run
```bash
# from the repo root
cd "Data Analysis Internship projects/Dashboards & AI"

# 0) Download and Unzip the bundle (first time only)
# Windows (PowerShell):
# Expand-Archive -Path ".\project files.zip" -DestinationPath "." -Force
# macOS/Linux:
# unzip -o "project files.zip" -d .

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
python -m ipykernel install --user --name week4 --display-name "Python (week4)"

# 4) Launch Jupyter
jupyter lab .    # or: jupyter notebook

# requirements.txt file
pandas
numpy
matplotlib
seaborn
jupyter
ipykernel

