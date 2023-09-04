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


# print(*possible_rolls, sep="\n")
# print("")
pprint(frequency_dict)
# print("")
# pprint(probability_dict)

# TODO write function to return dict of probabilities in simplified fractions (for readability)

# From two_on_one.py:
# TODO setup calc for prob of rolling either distance_1 OR distance 2
# note that rolling e.g. [5, 6] should not be counted twice
