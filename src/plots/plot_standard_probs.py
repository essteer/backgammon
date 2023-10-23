# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

palette = {
    "dark": "#252b33", "grey": "#45464d",
    "light": "#fefeff", "stone": "#8f8f94",
    "blue": "#336681", "green": "#089389",
    "red": "#d34748", "pink": "#cf82d3",
    "yellow": "#e6daaa"
}

# Create DataFrame from csv file
df = pd.read_csv("../data/backgammon_stats.csv")

# Set plot defaults
sns.set_style(rc={"figure.facecolor": palette["dark"],
                  "axes.facecolor": palette["dark"],
                  "axes.edgecolor": palette["light"],
                  "grid.color": palette["grey"]})


# Set up matplotlib figure
fig, ax = plt.subplots(figsize=(12, 9))

# Plot barplot
bar = sns.barplot(x=df["Move"],
                  y=df["Probability"],
                  hatch="//",
                  color=palette["red"],
                  ec=palette["grey"],
                  zorder=3)

# Remove top and right axes
sns.despine(offset=10)
# Remove ticks from x and y axes (left and bottom)
ax.tick_params(left=False, bottom=False)

# Set descriptors
bar.set_title("Moves by Probability - P(n)",
              fontdict={"size": 20,
                        "color": palette["light"]},
              pad=20)
bar.set_xlabel("n",
               fontdict={"size": 16, "color": palette["light"]},
               labelpad=10)
bar.set_ylabel("P(n)",
               fontdict={"size": 16, "color": palette["light"]},
               labelpad=10, 
               rotation=0)
plt.xticks(fontsize=16, color=palette["stone"])
plt.yticks(fontsize=16, color=palette["stone"])

# Remove leading zeros from y axis labels
ax.set_yticks([.0, .1, .2, .3, .4, .5])
new_yticks = [label.get_text().lstrip("0") for label in ax.get_yticklabels()]
ax.set_yticklabels(new_yticks)

# Show major gridlines
ax.grid(True,
        color=palette["grey"],
        linestyle="--",
        linewidth=0.5,
        zorder=0)

# Add text labels for probabilities as floats / % / true fractions
for bar in ax.patches:
    yval = bar.get_height()
    numerator = int(round(yval * 36))
    denominator = 36
    ax.text(bar.get_x() + bar.get_width()/2,
            yval + 0.005,  # adjust height above bar
            # display as floats
            # round(yval, 2),
            # display as percentages
            # f"{yval:.1%}",
            # display as true fractions
            f"${numerator}/{denominator}$",
            ha="center",
            va="bottom",
            color=palette["stone"],
            fontsize=12)

plt.tight_layout()
# fig.savefig("../images/moves_by_probability.png", dpi=300)

plt.show()
