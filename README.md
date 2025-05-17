# 🌞 Solar Challenge - Week 1

This project is part of the **Solar Data Analysis Challenge**. Week 1 focuses on repository setup, data cleaning, and exploratory data analysis (EDA) for solar datasets from multiple West African countries.

---

## 📁 Project Structure

```
solar-challenge-week1/
├── .github/
│   └── workflows/
│       └── ci.yml
├── data/                         
├── notebooks/                   
│   ├── benin_eda.ipynb
│   ├── sierra_leone_eda.ipynb
│   └── togo_eda.ipynb
├── .gitignore
├── requirements.txt
├── README.md
├── scripts/
│   └── README.md
├── tests/
│   └── __init__.py
└── venv/                         
```

---

## ✅ Task 1: Git & Environment Setup

### 📌 Objectives

* Get familiar with Git branching and version control.
* Set up reproducible Python environments.

### 🚀 Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Soloparame/solar-challenge-week1.git
   cd solar-challenge-week1
   ```

2. **Create Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Git Branches**

   * `setup-task`: contains initial setup, `.gitignore`, `ci.yml`
   * `eda-benin`, `eda-togo`, `eda-sierra-leone`: contain country-specific EDA notebooks

5. **GitHub Actions (CI)**

   * On every push, GitHub Actions installs requirements and checks environment.
   * Workflow file: `.github/workflows/ci.yml`

---

## 📊 Task 2: Data Profiling, Cleaning & EDA

Each EDA notebook follows a consistent structure:

### 🔍 EDA Steps Performed

| Step                  | Description                                             |
| --------------------- | ------------------------------------------------------- |
| 📃 Summary Stats      | `df.describe()`, missing value % check                  |
| 🧼 Cleaning           | Outlier detection (Z-score), NaN handling (impute/drop) |
| 📈 Time Series        | GHI, DNI, DHI, Tamb over time                           |
| 🧽 Cleaning Impact    | Compare ModA/B pre/post cleaning                        |
| 📉 Correlation        | Heatmaps, scatter plots (GHI, DNI, Tamb, WS, RH)        |
| 🌬️ Wind              | Histograms, wind direction analysis                     |
| 🌡️ Temperature vs RH | Bubble chart of Tamb vs GHI (size=RH)                   |
| 📀 Export             | Cleaned CSVs saved to `/data`, not committed to Git     |

### 📘 Notebooks

| Country      | Notebook Path                      | Branch             |
| ------------ | ---------------------------------- | ------------------ |
| Benin        | `notebooks/benin_eda.ipynb`        | `eda-benin`        |
| Sierra Leone | `notebooks/sierra_leone_eda.ipynb` | `eda-sierra-leone` |
| Togo         | `notebooks/togo_eda.ipynb`         | `eda-togo`         |

### 🧠 Insights Gained

* **Solar Irradiance Trends**: Seasonal and daily patterns visible across GHI, DNI, DHI.
* **Sensor Reliability**: Cleaning flags affect ModA/ModB performance.
* **Temperature Influence**: RH inversely correlates with Tamb and solar efficiency.
* **Wind Patterns**: Affect cleaning schedules and equipment wear.

---

## 📈 Git Best Practices Followed

* ✅ Feature branches per country (`eda-benin`, etc.)
* ✅ Descriptive commit messages
* ✅ `.gitignore` avoids committing large/irrelevant files
* ✅ GitHub Actions for CI (Python setup check)
* ✅ Pull requests for merging to `main`

---

## 📦 Requirements

All required libraries are listed in `requirements.txt`. Example:

```
pandas
numpy
matplotlib
seaborn
scikit-learn
```

---

## 🔐 .gitignore Highlights

```gitignore
# Ignore virtual environments
venv/
.env/

# Ignore data
data/*.csv

# Ignore notebooks' temp files
**/.ipynb_checkpoints/
```

---

## 📊 KPIs Achieved

* ✅ Environment setup & CI configured
* ✅ EDA notebooks with detailed visual insights
* ✅ Branching, committing, merging done cleanly
* ✅ Clear GitHub project structure for collaboration

---

## 👥 Contributors

* **Your Name** — EDA & Repo Setup
* Add other contributors if applicable...

---

## 📌 References

* [Matplotlib Docs](https://matplotlib.org/stable/index.html)
* [Pandas Profiling](https://pandas-profiling.github.io/)
* [Seaborn Gallery](https://seaborn.pydata.org/examples/index.html)

---
