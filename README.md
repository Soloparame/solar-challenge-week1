# 🌞 Solar Data Analysis Challenge — Week 1 Report

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
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── utils.py
├── tests/
│   └── __init__.py
└── venv/                         
```

---

## 🧩 Task 1 — Git & Environment Setup

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

## 📊 Task 2 — Data Profiling, Cleaning & EDA.

Each EDA notebook follows a consistent structure:

### 🔍 EDA Steps Performed

| Step                  | Description                                             |
| --------------------- | ------------------------------------------------------- |
| 📃 Summary Stats      | `df.describe()`, missing value % check                  |
| 🧬 Cleaning           | Outlier detection (Z-score), NaN handling (impute/drop) |
| 📈 Time Series        | GHI, DNI, DHI, Tamb over time                           |
| 🧽 Cleaning Impact    | Compare ModA/B pre/post cleaning                        |
| 📉 Correlation        | Heatmaps, scatter plots (GHI, DNI, Tamb, WS, RH)        |
| 🌬️ Wind              | Histograms, wind direction analysis                     |
| 🌡️ Temperature vs RH | Bubble chart of Tamb vs GHI (size=RH)                   |
| 📀 Export             | Cleaned CSVs saved to `/data`, not committed to Git     |

### 📘 Notebooks

| Country      | Notebook Path                                                | Branch             |
| ------------ | ------------------------------------------------------------ | ------------------ |
| Benin        | [`benin_eda.ipynb`](notebooks/benin_eda.ipynb)               | `eda-benin`        |
| Sierra Leone | [`sierra_leone_eda.ipynb`](notebooks/sierra_leone_eda.ipynb) | `eda-sierra-leone` |
| Togo         | [`togo_eda.ipynb`](notebooks/togo_eda.ipynb)                 | `eda-togo`         |

### 🧠 Insights Gained

* **Solar Irradiance Trends**: Seasonal and daily patterns visible across GHI, DNI, DHI.
* **Sensor Reliability**: Cleaning flags affect ModA/ModB performance.
* **Temperature Influence**: RH inversely correlates with Tamb and solar efficiency.
* **Wind Patterns**: Affect cleaning schedules and equipment wear.

---

## 🌍 Task 3 — Cross-Country Comparison & Streamlit Dashboard

This task involves both analytical comparison of solar data across countries and optional development of a dashboard.

### 🎯 Objectives

* Synthesize the cleaned datasets from Benin, Sierra Leone, and Togo.
* Identify relative solar potential and key differences across countries.
* Optionally, develop a Streamlit dashboard to visualize insights.

### 📒 Analysis Notebook

* Branch: `compare-countries`
* Notebook: `notebooks/compare_countries.ipynb`
* Data used: `data/benin_clean.csv`, `data/sierra_leone_clean.csv`, `data/togo_clean.csv`

### 📊 Analytical Components

* **Metric Comparison**

  * Boxplots of GHI, DNI, DHI (one plot per metric, color-coded by country)
  * Summary table comparing mean, median, standard deviation across countries
* **Statistical Testing (Recommended)**

  * One-way ANOVA or Kruskal–Wallis test for GHI values
  * Report and interpret p-values
* **Key Observations**

  * 3 bullet points summarizing standout insights (e.g., "Togo shows highest median GHI")
* **(Bonus) Visual Summary**

  * Bar chart ranking countries by average GHI

### 🌐 Streamlit Dashboard (Optional)

* Branch: `dashboard-dev`
* Main script: `app/main.py`
* Utility functions: `app/utils.py`

#### ⚙️ Features

| Feature               | Description                                 |
| --------------------- | ------------------------------------------- |
| Country Selector      | Widget to select one or multiple countries  |
| Boxplot Visualization | Interactive boxplot of GHI/DNI/DHI          |
| Top Regions Table     | Table showing top solar regions per country |
| CSV Export            | Download option for filtered data           |

### 🚀 Deployment

* Hosted via Streamlit Community Cloud (see [how to deploy](https://docs.streamlit.io/streamlit-community-cloud/get-started/deploy-an-app))
* To run locally:

  ```bash
  streamlit run app/main.py
  ```

### 📂 Suggested Folder Structure

```
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── utils.py
└── scripts
    ├── __init__.py
    └── README.md
```

### 📈 Key Performance Indicators (KPIs)

* [x] Inclusion of all three countries in comparisons
* [x] Correct implementation and interpretation of p-values
* [x] Actionable summary insights
* [x] Clean UI/UX in dashboard (if built)
* [x] Working widgets and interactive elements
* [x] Public deployment (optional)

---

## 🧾 Git Best Practices Followed.


* ✅ Feature branches per country (`eda-benin`, etc.)
* ✅ Descriptive commit messages
* ✅ `.gitignore` avoids committing large/irrelevant files
* ✅ GitHub Actions for CI (Python setup check)
* ✅ Pull requests for merging to `main`

---

## 📦 Requirements.

All required libraries are listed in `requirements.txt`

## 🔐 .gitignore Highlights.

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

* [x] Environment setup & CI configured
* [x] EDA notebooks with detailed visual insights
* [x] Streamlit dashboard with comparative analytics
* [x] Branching, committing, merging done cleanly
* [x] Clear GitHub project structure for collaboration

## 📌 References

* [Matplotlib Docs](https://matplotlib.org/stable/index.html)
* [Pandas Profiling](https://pandas-profiling.github.io/)
* [Seaborn Gallery](https://seaborn.pydata.org/examples/index.html)
* [Streamlit Docs](https://docs.streamlit.io/)

---
