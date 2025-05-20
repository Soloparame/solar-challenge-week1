# 🌞 Solar Challenge - Week 1

## 🔧 Environment Setup

Follow these steps to set up and reproduce the development environment:

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/solar-challenge-week1.git
   cd solar-challenge-week1
   ```

2. **Create a virtual environment**

   * Using `venv`:

     ```bash
     python3 -m venv venv
     source venv/bin/activate        # On Windows: venv\Scripts\activate
     ```

   * Using `conda`:

     ```bash
     conda create -n solar_challenge python=3.10 -y
     conda activate solar_challenge
     ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run CI workflow**

   * Push changes to GitHub to trigger GitHub Actions.
   * Or run CI manually from the GitHub Actions tab.

---

## 📁 Folder Structure

```
solar-challenge-week1/
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows/
│       └── ci.yml
├── app/
│   ├── __init__.py
│   ├── main.py                # Streamlit app entry point
│   └── utils.py               # Data loading, plotting, summarizing
├── data/
│   ├── benin_clean.csv
│   ├── sierraleone_clean.csv
│   └── togo_clean.csv
├── notebooks/
│   ├── __init__.py
│   └── README.md
├── scripts/
│   ├── __init__.py
│   └── README.md
├── tests/
│   └── __init__.py
├── requirements.txt
└── README.md
```

---

## ✅ Tasks Summary

### ✔️ Task 1: Data Cleaning

* Cleaned solar irradiation datasets for Benin, Sierra Leone, and Togo.
* Addressed missing values, outliers, and unified formats.
* Outputs saved as `*_clean.csv` in the `/data/` folder.

### ✔️ Task 2: CI Integration

* GitHub Actions configured for basic CI pipeline.
* Workflow file located at `.github/workflows/ci.yml`.

---

## 📊 Task 3: Cross-Country Solar Data Comparison Dashboard

A **Streamlit dashboard** was developed to visualize and compare solar energy metrics (`GHI`, `DNI`, `DHI`) across Benin, Sierra Leone, and Togo.

### 🚀 Features

* Country selection dropdown.
* Metric selection (`GHI`, `DNI`, `DHI`).
* Interactive boxplots.
* Summary statistics table.

### 📂 Files

* `app/main.py`: Main dashboard logic.
* `app/utils.py`: Helper functions to load data, plot, and summarize.

### ▶️ Running the Dashboard Locally

```bash
streamlit run app/main.py
```



