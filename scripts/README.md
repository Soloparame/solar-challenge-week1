# 🌍 Solar Dashboard

## 🔧 How to Run
```bash
# Create and activate a virtual environment (recommended)
python -m venv venv
venv\Scripts\activate  # Windows

# Install requirements
pip install streamlit pandas matplotlib seaborn

# Run the dashboard
streamlit run app/main.py
```

## 📌 Features
- Interactive country selector
- Boxplots for GHI, DNI, DHI
- Summary tables
- Modular & scalable code structure

## 🚜 Git Hygiene
- Ensure `data/` is in `.gitignore`
- Do **not** push local CSV files
- Commit with clear messages:
```bash
git add .
git commit -m "feat: basic Streamlit dashboard with boxplot and stats"
```

## ✅ Example Commit Message
```
feat: add interactive Streamlit dashboard for solar metrics
