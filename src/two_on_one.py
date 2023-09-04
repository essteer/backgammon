# -*- coding: utf-8 -*-
from helpers.rolls import compute_rolls
from helpers.frequencies import compute_frequencies
from helpers.probabilities import compute_probabilities
from pprint import pprint

# Call function to generate list of lists of possible roll outcomes
# Defaults to two six-sided dice
possible_rolls = compute_rolls()

# Call function to generate dict for frequencies of each roll in possible_rolls
frequency_dict = compute_frequencies(possible_rolls)

# Call function to generate dict for probabilities of rolls in frequency_dict
probability_dict = compute_probabilities(frequency_dict)

# print("")
# pprint(frequency_dict)
# print("")
# pprint(probability_dict)

# Set number of spaces needed to land a player's pieces on their opponent's piece:
distance_1 = 5
distance_2 = 6

prob_1 = probability_dict[distance_1]
prob_2 = probability_dict[distance_2]

print(
    f"Prob. of landing on opponent's piece {distance_1} spaces away: {prob_1:.2f}")
print(
    f"Prob. of landing on opponent's piece {distance_2} spaces away: {prob_2:.2f}")
print("")

# TODO setup calc for prob of rolling either distance_1 OR distance 2
# note that rolling e.g. [5, 6] should not be counted twice
