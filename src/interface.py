# -*- coding: utf-8 -*-
from helpers.rolls import compute_rolls
from helpers.frequencies import compute_frequencies
from helpers.probabilities import compute_probabilities
from helpers.combinations import combination_moves
from helpers.obstacles import add_obstacles
import pandas as pd

DISTANCE_1 = 3
DISTANCE_2 = 13
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
# Sense checks
##########################################################################

# 6*6 = 36 possible outcomes from two six-sided dice 
assert len(possible_rolls)   == 36
# 17 distinct value outcomes:
#     1 to 12 via standard die values
#     15, 16, 18, 20, 24 via doubles rule
assert len(freq_dict) == 17
assert len(prob_dict) == 17
# 1/36 chance of double outcomes
assert round(1/36, 4) == prob_dict[15] == prob_dict[16] == prob_dict[18] == prob_dict[20] == prob_dict[24]

print("Sense checks passed")

##########################################################################
# Create DataFrame of individual probabilities
##########################################################################

# Create DataFrame for stats_list
columns = ["Move", "Frequency", "Probability"]
df = pd.DataFrame(stats_list, columns=columns)
# Save DataFrame to csv
# df.to_csv("./data/backgammon_stats.csv")

##########################################################################
# Query data
##########################################################################

# Print probabilities for possible moves between 1 <= x <= 24
for stat in stats_list:
    print(
        f"Prob. able to land {stat[0]} space{'s' if stat[0] != 1 else ''} away: {stat[2]:.2%}")

# Test probabilities for reaching two distances
combination_frequencies = combination_moves(
    possible_rolls,
    DISTANCE_1,
    DISTANCE_2)

print(
    f"Prob. able to land from either {DISTANCE_1} or {DISTANCE_2} spaces away: {combination_frequencies/36:.2%}")


# Test use of obstacles
# obstructed_combination_frequencies = add_obstacles(
#     possible_rolls,
#     DISTANCE_1,
#     DISTANCE_2,
#     OBSTACLES)

# print(
#     f"Prob. able to land from either {DISTANCE_1} or {DISTANCE_2} spaces away: {obstructed_combination_frequencies/36:.2%}")

##########################################################################
# Sense checks
##########################################################################