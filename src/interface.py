# -*- coding: utf-8 -*-
from helpers.rolls import compute_rolls
from helpers.frequencies import compute_frequencies
from helpers.probabilities import compute_probabilities
from helpers.combinations import combination_moves
from helpers.obstacles import add_obstacles

# Generate list of lists of possible roll outcomes
possible_rolls = compute_rolls()
# Generate dict for frequencies of each roll in possible_rolls
frequency_dict = compute_frequencies(possible_rolls)
# Generate dict for probabilities of rolls in frequency_dict
probability_dict = compute_probabilities(frequency_dict)
# Create sorted list of keys in probability_dict for ordered display
probability_dict_keys = [k for k in probability_dict]
probability_dict_keys.sort()

# Print out probabilities for possible moves between 1 <= x <= 24
# for k in probability_dict_keys:
#     print(
#         f"Prob. able to land {k} space{'s' if k != 1 else ''} away: {probability_dict[k]:.2%}")

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
