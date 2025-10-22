# Week 04 — Dashboards & AI

**Goal:** Explore and communicate key business metrics using interactive dashboards.
This week, package the data prep notebook(s), Tableau workbook, and report in a single archive so others can reproduce the exports and view the dashboards.

---

## Files in this folder
- `project files.zip` — contains notebooks, datasets, and the Tableau workbook (and/or data extracts)
- `Week4-Project Brief-Dashboards & AI.pdf` — project brief with the **Tableau dashboard link**


### 1) Download and Unzip the project bundle
**Windows (PowerShell):**
```powershell
Expand-Archive -Path ".\project files.zip" -DestinationPath "." -Force

**macOS/ Linux:**
unzip -o "project files.zip" -d .

# from the repo root, cd into the Week 04 folder
cd "Data Analysis Internship projects/Dashboards & AI"

# 1) Create & activate a virtual env
python -m venv .venv
# Windows PowerShell:
. .\.venv\Scripts\Activate.ps1
# macOS/Linux:
# source .venv/bin/activate

# 2) Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt   # create this file (see below)

# 3) Make Jupyter see this env (once)
python -m ipykernel install --user --name week4 --display-name "Python (week4)"

# 4) Launch Jupyter
jupyter lab .    # or: jupyter notebook

requirements.txt
pandas
numpy
matplotlib
seaborn
jupyter
ipykernel

