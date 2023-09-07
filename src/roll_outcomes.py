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

# Create sorted list of keys in probability_dict
probability_dict_keys = [k for k in probability_dict]
probability_dict_keys.sort()

for k in probability_dict_keys:
    print(
        f"Prob. able to land {k} space{'s' if k != 1 else ''} away: {100*probability_dict[k]:.2f}%")
