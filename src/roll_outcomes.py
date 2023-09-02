# -*- coding: utf-8 -*-
from helpers.frequencies import compute_frequencies
from helpers.probabilities import compute_probabilities
from pprint import pprint

possible_rolls = []
# Generate possible outcomes from rolling two fair six-sided dice
for i in range(1, 7):
    for j in range(1, 7):
        if i == j:
            # Backgammon rules: doubles yield four moves
            # E.g. rolling [3, 3] gives a player the move options [3, 3, 3, 3]
            possible_rolls.append([i]*4)
        else:
            possible_rolls.append([i, j])

# Call function to generate dict for frequencies of each roll in possible_rolls
frequency_dict = compute_frequencies(possible_rolls)

# Call function to generate dict for probabilities of rolls in frequency_dict
probability_dict = compute_probabilities(frequency_dict)

# TODO write function to return dict of probabilities in simplified fractions (for readability)

# print(*possible_rolls, sep="\n")
# print("")
# pprint(frequency_dict)
print("")
pprint(probability_dict)
