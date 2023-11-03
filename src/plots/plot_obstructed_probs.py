# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import pandas as pd
import seaborn as sns
from typing import Literal

PLOT: Literal["decimal", "fraction"] = "fraction"

palette = {
    "dark": "#252b33", "grey": "#45464d",
    "light": "#fefeff", "stone": "#8f8f94",
    "blue": "#336681", "green": "#089389",
    "red": "#d34748", "pink": "#cf82d3",
    "yellow": "#e6daaa"
}

# Create DataFrames from csv file
probs_df = pd.read_csv("../data/obstructed_probs.csv")
freqs_df = pd.read_csv("../data/obstructed_freqs.csv")

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

if PLOT == "decimal":
    # Plot the heatmap
    hmap = sns.heatmap(probs_df.transpose(),  # swap the axes
                       xticklabels=probs_df.columns, 
                       yticklabels=probs_df.columns,
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

elif PLOT == "fraction":
    # Plot the heatmap
    hmap = sns.heatmap(freqs_df.transpose(),  # swap the axes 
                       xticklabels=probs_df.columns, 
                       yticklabels=probs_df.columns,
                       annot=True, 
                       annot_kws={"size": 12},
                       linewidth=0.5, 
                       cmap=custom_cmap, 
                       linecolor=palette["dark"],
                       cbar_kws={"pad": 0.02}
                       )
    # Set annotations to fractions / 36
    for text in hmap.texts:
        text.set_text(f"{text.get_text()}/36")

# Remove ticks from x and y axes (left and bottom)
hmap.tick_params(left=False, bottom=False)
# Remove ticks from cbar
cbar = ax.collections[0].colorbar
cbar.ax.tick_params(right=False)

# Set descriptors
hmap.set_title("Obstructed Move Probability - P(n not k)",
              fontdict={"size": 20,
                        "color": palette["light"]},
              pad=20)
hmap.set_xlabel("n",
               fontdict={"size": 16, "color": palette["light"]},
               labelpad=10)
hmap.set_ylabel("k",
               fontdict={"size": 16, "color": palette["light"]},
               labelpad=10,
               rotation=0)

plt.xticks(fontsize=16, color=palette["stone"])
plt.yticks(fontsize=16, color=palette["stone"], rotation=0)
cbar.ax.tick_params(labelsize=16, labelcolor=palette["stone"])

if PLOT == "decimal":
    cbar.set_ticks([0.1, 0.2, 0.3, 0.4])
    cbar.set_ticklabels([".1", ".2", ".3", ".4"])

elif PLOT == "fraction":
    # cbar.set_ticks([1, 3, 6, 9, 12, 15])
    cbar.set_ticks([1, 4, 7, 10, 13, 16])
    cbar.set_ticklabels(["1/36", "1/9", "7/36", "10/36", "13/36", "4/9"])

plt.tight_layout()

if PLOT == "decimal":
    fig.savefig("../images/obstructed_prob_dec.png", 
                dpi=300,
                bbox_inches="tight")

elif PLOT == "fraction":
    fig.savefig("../images/obstructed_prob_frac.png", 
                dpi=300,
                bbox_inches="tight")

plt.show()
