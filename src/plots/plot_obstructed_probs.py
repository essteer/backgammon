# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
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
df = pd.read_csv("../data/obstructed_probs.csv")

# Set plot defaults
sns.set_style(rc={"figure.facecolor": palette["dark"],
                  "axes.facecolor": palette["dark"],
                  "axes.edgecolor": palette["light"],
                  "grid.color": palette["grey"]})

# Select heatmap colours
hmap_colours = [palette["blue"], palette["dark"], palette["red"]]
# Define colour boundaries and corresponding values
bounds = [0, 0.25, 1]
# bounds = [0, 0.15, 0.35, 1]
norm = mcolors.BoundaryNorm(bounds, len(hmap_colours))

# Create the colourmap
custom_cmap = mcolors.LinearSegmentedColormap.from_list("", list(zip(bounds, hmap_colours)))

# Set up matplotlib figure
fig, ax = plt.subplots(figsize=(12, 9))

# Plot the heatmap
hmap = sns.heatmap(df, 
                   xticklabels=df.columns, 
                   yticklabels=df.columns,
                   annot=True, 
                   annot_kws={"size": 12},
                   fmt=".3f", 
                   linewidth=0.5, 
                   cmap=custom_cmap, 
                   linecolor=palette["dark"],
                   cbar_kws={"pad": 0.02}
                   )

# Remove leading zeros from annotations
for text in hmap.texts:
    text.set_text(text.get_text().lstrip("0"))

# Remove ticks from x and y axes (left and bottom)
hmap.tick_params(left=False, bottom=False)
# Remove ticks from cbar
cbar = ax.collections[0].colorbar
cbar.ax.tick_params(right=False)

# Set descriptors
hmap.set_title("Move Probability with Obstacles - P(n not k)",
              fontdict={"size": 20,
                        "color": palette["light"]},
              pad=20)
hmap.set_xlabel("k",
               fontdict={"size": 16, "color": palette["light"]},
               labelpad=10)
hmap.set_ylabel("n",
               fontdict={"size": 16, "color": palette["light"]},
               labelpad=10,
               rotation=0)

plt.xticks(fontsize=16, color=palette["stone"])
plt.yticks(fontsize=16, color=palette["stone"], rotation=0)
cbar.ax.tick_params(labelsize=16, labelcolor=palette["stone"])

cbar.set_ticks([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7])
cbar.set_ticklabels([".1", ".2", ".3", ".4", ".5", ".6", ".7"])

plt.tight_layout()
fig.savefig("../images/obstructed_probability.png", 
            dpi=300,
            bbox_inches="tight")

plt.show()