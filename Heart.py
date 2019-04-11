# -*- coding: utf-8 -*-
"""
Problem:  Create a word frequency algorithm without using a library
Authur: Claudius Taylor
"""
# load libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import cufflinks as cf

df = pd.read_csv("http://www-bcf.usc.edu/~gareth/ISL/Heart.csv", index_col=0)
df.head()

heart_rate_df = df[df["AHD"] == "Yes"]
counts = heart_rate_df.groupby("ChestPain")["RestBP"].count()
count_df = pd.DataFrame(counts)
count_df.columns = ['Count']
count_df.sort_values(by=['Count'], inplace=True, ascending=False)
count_df.index.name = "ChestPain"
count_df.head()

cf.go_offline()
count_df.iplot(title="Heart Rate",
               yTitle="Count",
               kind="bar",
               shape=(4,1),
               fill=True)

df['Age'].iplot(kind='hist', bins=20)

# import plotly and offline mode
from plotly.offline import iplot, init_notebook_mode
import plotly.graph_objs as go
data = []

for col in df['Thal'].unique():
    data.append(go.Box(y=df[df['Thal'] == col]['Age'], name=col, showlegend=True))

iplot(data)


sns.lmplot(x='Chol', y='Age', data=df)