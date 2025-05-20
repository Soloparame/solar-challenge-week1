import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils import load_data, plot_boxplot, summary_table

st.title("🌞 Solar Data Dashboard")

country = st.selectbox("Select Country", ["Benin", "Sierra Leone", "Togo"])
data_path = f"data/{country.lower().replace(' ', '')}_clean.csv"
df = load_data(data_path)

plot_metric = st.selectbox("Metric", ["GHI", "DNI", "DHI"])
fig = plot_boxplot(df, plot_metric)
st.pyplot(fig)

st.subheader("📊 Summary Table")
st.dataframe(summary_table(df, ["GHI", "DNI", "DHI"]))
