import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(path):
    return pd.read_csv(path)

def plot_boxplot(df, metric):
    fig, ax = plt.subplots()
    sns.boxplot(data=df, y=metric, ax=ax)
    ax.set_title(f"{metric} Distribution")
    return fig

def summary_table(df, columns):
    summary = df[columns].agg(['mean', 'median', 'std']).T
    summary.columns = ['Mean', 'Median', 'Std Dev']
    summary = summary.round(2)
    return summary
