# -*- coding: utf-8 -*-
from helpers.rolls import compute_rolls
from helpers.frequencies import compute_frequencies
from helpers.probabilities import compute_probabilities
from helpers.combinations import combination_moves
from helpers.obstacles import add_obstacles
import pandas as pd

# Generate list of lists of possible roll outcomes
possible_rolls = compute_rolls()
# Generate dict for frequencies of each roll in possible_rolls
frequency_dict = compute_frequencies(possible_rolls)
# Generate dict for probabilities of rolls in frequency_dict
probability_dict = compute_probabilities(frequency_dict)
# Create list of lists of frequencies and probabilities per possible move
stats_list = [[key, frequency_dict[key], probability_dict[key]]
              for key in sorted(frequency_dict.keys())]
# Create DataFrame for stats_list
columns = ["Move", "Frequency", "Probability"]
df = pd.DataFrame(stats_list, columns=columns)
# Save DataFrame to csv
# df.to_csv("./data/backgammon_stats.csv")

# Print out probabilities for possible moves between 1 <= x <= 24
# for stat in stats_list:
#     print(
#         f"Prob. able to land {stat[0]} space{'s' if stat[0] != 1 else ''} away: {stat[2]:.2%}")

# Test probabilities for reaching two distances
# distance_1 = 12
# distance_2 = 12
# combination_frequencies = combination_moves(
#     possible_rolls,
#     distance_1,
#     distance_2)

# print(
#     f"Prob. able to land from either {distance_1} or {distance_2} spaces away: {combination_frequencies/36:.2%}")


# Test use of obstacles
# distance_1 = 3
# distance_2 = 19
# test_obstacles = [1, 2]
# obstructed_combination_frequencies = add_obstacles(
#     possible_rolls,
#     distance_1,
#     distance_2,
#     test_obstacles)

# print(
#     f"Prob. able to land from either {distance_1} or {distance_2} spaces away: {obstructed_combination_frequencies/36:.2%}")
