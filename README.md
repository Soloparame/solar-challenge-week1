# 🌞 Solar Electrification Challenge – Week 0 Report

## 🔧 Project Setup

This repository contains the Week 0 progress for the Solar Electrification Challenge, focusing on data cleaning, exploration, and comparison across three countries: **Benin**, **Togo**, and **Sierra Leone**.

---

## 📁 Directory Structure

├── data/ # Raw input datasets
├── outputs/ # Cleaned datasets and visualizations
├── dashboard-dev/ # Streamlit dashboard development branch
├── notebooks/ # Jupyter Notebooks for EDA and cleaning
├── .github/workflows/ # CI workflow files
├── requirements.txt # Python dependencies
└── README.md # Project documentation

yaml
Copy
Edit

---

## ✅ Tasks Completed in Week 0

### 1. Exploratory Data Analysis (EDA)
- Loaded and analyzed all datasets
- Identified missing values, duplicates, outliers
- Created visual summaries using seaborn and matplotlib

### 2. Data Cleaning
- Unified schemas across the three datasets
- Imputed missing values, removed duplicates
- Standardized column names and data types
- Exported cleaned CSVs to `outputs/`

### 3. Cross-Country Comparison
- Compared technology usage, demand tiers, and grid proximity
- Visualized differences using bar plots, pie charts, and scatter plots
- Summarized insights in notebooks and prepared visuals for the dashboard

---

## ⚠️ CI/CD Fixes and Dependency Issues

### 🛠 Issue: Build Failed on GitHub Actions

The GitHub Actions CI pipeline failed during the **Install Dependencies** step due to a `pandas` build error:

> `error: standard attributes in middle of decl-specifiers`

### 🔍 Root Cause

- `pandas==2.2.2` was incompatible with the Python version (likely Python 3.13)
- Certain Cython-based modules could not be compiled due to compiler incompatibility

### ✅ Solution Applied

#### 1. **Locked Python Version to 3.11**
Updated `.github/workflows/ci.yml`:
```yaml
- name: Set up Python
  uses: actions/setup-python@v4
  with:
    python-version: '3.11'
2. Pinned pandas to a Stable Version
Updated requirements.txt:

diff
Copy
Edit
- pandas==2.2.2
+ pandas==2.1.3
3. Cleared pip Cache Before Installing
Added to CI workflow:

yaml
Copy
Edit
- name: Clear pip cache
  run: |
    pip cache purge
4. Local Testing Done
Tested the environment locally with:

bash
Copy
Edit
python -m venv env
source env/bin/activate
pip install -r requirements.txt
🟢 Result
CI/CD now runs successfully with all dependencies installed and notebooks tested.

🚀 How to Run the Project Locally
bash
Copy
Edit
# Clone the repo
git clone https://github.com/your-username/solar-challenge-week1.git
cd solar-challenge-week1

# Set up environment
python -m venv env
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run dashboard (after Week 1)
streamlit run dashboard-dev/app.py
📊 Preview
EDA visualizations: notebooks/eda_summary.ipynb

Cleaned CSVs: outputs/

Dashboard preview: Work in progress in dashboard-dev

📎 Useful Links
Workflow File: .github/workflows/ci.yml

Requirements: requirements.txt

Cleaned Data: /outputs/

Dashboard Dev Branch: dashboard-dev


📅 Status
✅ Week 0 tasks completed
🔄 Dashboard development in progress for Week 1
