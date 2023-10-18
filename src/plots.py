# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Create DataFrame from csv file
df = pd.read_csv("data/backgammon_stats.csv")

# Set plot defaults
sns.set_style(rc={"figure.facecolor": "#252b33",
                  "axes.facecolor": "#252b33",
                  "axes.edgecolor": "#fefeff",
                  "grid.color": "#45464d",
                  "text.usetext": "tex"})


# Set up matplotlib figure
fig, ax = plt.subplots(figsize=(12, 9))

# Plot barplot
bar = sns.barplot(x=df["Move"],
                  y=df["Probability"],
                  hatch="//",
                  color="#d34748",
                  ec="#45464d",
                  zorder=3)

# Remove top and right axes
sns.despine(offset=10)
# Remove ticks from x and y axes (left and bottom)
ax.tick_params(left=False, bottom=False)

# Set descriptors
bar.set_title("Backgammon Moves by Probability",
              fontdict={"size": 20,
                        "color": "#fefeff"})
bar.set_xlabel("Move (Number of Spaces)",
               fontdict={"size": 16, "color": "#fefeff"})
bar.set_ylabel("Probability",
               fontdict={"size": 16, "color": "#fefeff"})
plt.xticks(fontsize=16, color="#8f8f94")
plt.yticks(fontsize=16, color="#8f8f94")

# Show major gridlines
ax.grid(True,
        color='#45464d',
        linestyle='--',
        linewidth=0.5,
        zorder=0)

# Add text labels for probabilities as floats
# for bar in ax.patches:
#     yval = bar.get_height()
#     ax.text(bar.get_x() + bar.get_width()/2,
#             yval + 0.005,
#             round(yval, 2),
#             ha='center',
#             va='bottom',
#             color='#8f8f94',
#             fontsize=12)


# Add text labels for probabilities as percentages
# for bar in ax.patches:
#     yval = bar.get_height()
#     ax.text(bar.get_x() + bar.get_width()/2,
#             yval + 0.005,  # adjust height above bar
#             f"{yval:.1%}",
#             ha="center",
#             va="bottom",
#             color="#8f8f94",
#             fontsize=12)

# Add text labels for probabilities as true fractions
for bar in ax.patches:
    yval = bar.get_height()
    numerator = int(round(yval * 36))
    denominator = 36
    ax.text(bar.get_x() + bar.get_width()/2,
            yval + 0,  # adjust height above bar
            f'${numerator}/{denominator}$', ha='center',
            va='bottom',
            color='#8f8f94',
            fontsize=12)

fig.savefig("./plots/moves_by_probability.png")

plt.show()
