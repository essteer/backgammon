# -*- coding: utf-8 -*-
from helpers.rolls import compute_rolls
from helpers.frequencies import compute_frequencies
from helpers.probabilities import compute_probabilities
from helpers.combinations import combination_moves
from helpers.obstacles import add_obstacles
import numpy as np
import pandas as pd

# Rounding digits
R = 4
# Test distances for assert statements
TESTS = {"A": 7, "B": 13, "C": 10, "D": 15, "E": 4, "F": 0}
# Obstructed spaces for tests
OBSTACLES = [1, 2]

##########################################################################
# Create data
##########################################################################

# Generate list of lists of possible roll outcomes
possible_rolls = compute_rolls()
# Generate dict for frequencies of each roll in possible_rolls
freq_dict = compute_frequencies(possible_rolls)
# Generate dict for probabilities of rolls in freq_dict
prob_dict = compute_probabilities(freq_dict)
# Create list of lists of frequencies and probabilities per possible move
stats_list = [[key, freq_dict[key], prob_dict[key]]
              for key in sorted(freq_dict.keys())]

##########################################################################
# Sense check
##########################################################################

# ~~~ Standard probabilities ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 6*6 = 36 possible outcomes from two six-sided dice 
assert len(possible_rolls) == 36
# 17 distinct value outcomes:
#     1 to 12 via standard die values
#     15, 16, 18, 20, 24 via doubles rule
assert len(freq_dict) == 17
assert len(prob_dict) == 17
# P = 1/36 for extended double outcomes
assert round(1/36, R) == prob_dict[15] == prob_dict[16] == prob_dict[18] == prob_dict[20] == prob_dict[24]

# ~~~ Combined probabilities ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# P(A or B) == P(A), where P(B) == 0
assert combination_moves(possible_rolls, TESTS["A"], TESTS["B"])/36 == freq_dict[TESTS["A"]]/36
# P(A or B) == P(B), where P(A) == 0
assert combination_moves(possible_rolls, TESTS["B"], TESTS["A"])/36 == freq_dict[TESTS["A"]]/36
# P(A or B) == P(A) == P(B), where A == B
assert combination_moves(possible_rolls, TESTS["A"], TESTS["A"])/36 == freq_dict[TESTS["A"]]/36

# P(C or D) == P(C) + P(D) - P(C and D)
f_C = freq_dict[TESTS["C"]]  # C achieved via [4, 6], [5, 5], or [6, 4]
f_D = freq_dict[TESTS["D"]]  # D achieved via [5, 5]
n = 1  # (C and D) achieved via single case [5, 5]
assert combination_moves(possible_rolls, TESTS["C"], TESTS["D"]) == f_C + f_D - n
f_A = freq_dict[TESTS["A"]]  # A achieved via 15 combinations
f_E = freq_dict[TESTS["E"]]  # E achieved via 6 combinations
n = 2  # (A and E) achieved via two cases [3, 4], [4, 3]
assert combination_moves(possible_rolls, TESTS["A"], TESTS["E"]) == f_A + f_E - n

print("Sense checks passed")

##########################################################################
# Create DataFrames
##########################################################################

# ~~~ Standard probabilities ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Create DataFrame for stats_list
columns = ["Move", "Frequency", "Probability"]
standard_df = pd.DataFrame(stats_list, columns=columns)
# Save DataFrame to csv
# standard_df.to_csv("./data/backgammon_stats.csv")

# ~~~ Combined probabilities ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# List of possible distances
distances = np.array([key for key in sorted(freq_dict.keys())])
# Create meshgrid of all distance combinations
distance_1, distance_2 = np.meshgrid(distances, distances)

results = []
# Iterate through each combination of distances
for d1, d2 in zip(distance_1.flatten(), distance_2.flatten()):
    # Calculate combined frequencies for distance pair
    combined_freq = combination_moves(possible_rolls, d1, d2)
    # Calculate combined probabilities for distance pair
    combined_prob = np.round(combined_freq / 36, R)
    # Append to results
    results.append([d1, d2, combined_prob])

# Create DataFrame for combined_probabilities
combined_df = pd.DataFrame(results, columns=["Distance 1", "Distance 2", "Combined Probability"])
# Pivot the DataFrame
pivot_cdf = combined_df.pivot(index="Distance 1", columns="Distance 2", values="Combined Probability")
pivot_cdf = pivot_cdf.fillna(0.)

# Save DataFrame to csv
# pivot_cdf.to_csv("./data/combined_probs.csv", index=False)

# ~~~ Obstructed probabilities ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# List of possible distances and obstacles
distances = np.array([key for key in sorted(freq_dict.keys())])
# Create meshgrid of distance-obstacle pairs
distance_1, obstacle = np.meshgrid(distances, distances)

obstacle_results = []
# Iterate through each distance-obstacle pair
for d1, o1 in zip(distance_1.flatten(), obstacle.flatten()):
    # Calculate combined frequencies
    obstructed_freq = add_obstacles(possible_rolls, d1, 0, [o1])
    # Calculate combined probabilities
    obstructed_prob = np.round(obstructed_freq / 36, R)
    # Append to results
    obstacle_results.append([d1, o1, obstructed_prob])

# Create DataFrame for obstructed_probabilities
obstructed_df = pd.DataFrame(obstacle_results, columns=["Distance", "Obstacle", "Obstructed Probability"])
# Pivot the DataFrame
pivot_odf = obstructed_df.pivot(index="Distance", columns="Obstacle", values="Obstructed Probability")
pivot_odf = pivot_odf.fillna(0.)

# Save DataFrame to csv
pivot_odf.to_csv("./data/obstructed_probs.csv", index=False)

##########################################################################
# Query individual data points
##########################################################################

# Print probabilities for possible moves between [1, 24]
# for stat in stats_list:
#     print(
#         f"Prob. able to land {stat[0]} space{'s' if stat[0] != 1 else ''} away: {stat[2]:.2%}")

# Test use of obstacles
# obstructed_combination_frequencies = add_obstacles(
#     possible_rolls,
#     TESTS["A"],
#     TESTS["B"],
#     OBSTACLES)

# print(
#     f"Prob. able to land from either {TESTS["A"]} or {TESTS["B"]} spaces away: {obstructed_combination_frequencies/36:.2%}")
