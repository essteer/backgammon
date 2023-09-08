# -*- coding: utf-8 -*-
from helpers.rolls import compute_rolls
from helpers.frequencies import compute_frequencies
from helpers.probabilities import compute_probabilities
from helpers.combinations import combination_moves
from pprint import pprint

# Call function to generate list of lists of possible roll outcomes
# Defaults to two six-sided dice
possible_rolls = compute_rolls()

# Call function to generate dict for frequencies of each roll in possible_rolls
frequency_dict = compute_frequencies(possible_rolls)

# Call function to generate dict for probabilities of rolls in frequency_dict
probability_dict = compute_probabilities(frequency_dict)

# Create sorted list of keys in probability_dict for ordered display
probability_dict_keys = [k for k in probability_dict]
probability_dict_keys.sort()

for k in probability_dict_keys:
    print(
        f"Prob. able to land {k} space{'s' if k != 1 else ''} away: {100*probability_dict[k]:.2f}%")


distance_1 = 8
distance_2 = 12
combination_frequencies = combination_moves(
    possible_rolls, distance_1, distance_2)

print(
    f"Prob. able to land from either {distance_1} or {distance_2} spaces away: {100*(combination_frequencies/36):.2f}%")
