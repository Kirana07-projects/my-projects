# Week 03 — Predictive Modelling with Python (Churn Prediction)

**Goal:** Build and evaluate a churn-propensity model for **StreamWorks Media**. The workflow covers data loading, cleaning, feature engineering, train/validation split, model training, evaluation (ROC-AUC, precision/recall/F1, confusion matrix), threshold tuning, and actionable insights.

## Files in this folder
- `Week 3 - Churn Prediction for StreamWorks Media.ipynb` — main notebook (ETL ➜ modelling ➜ evaluation)
- `Week 3 Churn Prediction for StreamWorks Media.pdf` — report/slide deck for this task
- `Project Files/` — input dataset folder used by the notebook (see **Data access**)

## Data access
- streamworks_user_data.csv' - file used for this project task

# from the repo root, cd into the Week 03 folder
cd "Data Analysis Internship projects/Predictive Modelling with Python"

# 1) Create & activate a virtual env
python -m venv .venv
# Windows PowerShell:
. .\.venv\Scripts\Activate.ps1
# macOS/Linux:
# source .venv/bin/activate

# 2) Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt   # create this file with the list below

# 3) Make Jupyter see this env (once)
python -m ipykernel install --user --name week3 --display-name "Python (week3)"

# 4) Launch Jupyter
jupyter lab .    # or: jupyter notebook

# Create a file called requirements.txt with the following libraries
pandas
numpy
scikit-learn
matplotlib
seaborn
jupyter
ipykernel


