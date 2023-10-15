# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
import pandas as pd
import seaborn as sns

# Create DataFrame from csv file
df = pd.read_csv("data/backgammon_stats.csv")

# Set plot defaults
sns.set_style(rc={"axes.facecolor": "#3d405b"})
# Set up matplotlib figure
fig, ax = plt.subplots(figsize=(12, 9))
# Plot barplot
bar = sns.barplot(x=df["Move"],
                  y=df["Probability"],
                  hatch="//",
                  color="#bc4b51",
                  ec="#f4f1de")

plt.title("Backgammon Moves by Probability", fontsize=30)
plt.xlabel("Move (Number of Spaces)", fontsize=22)
plt.ylabel("Probability", fontsize=22)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.show()
