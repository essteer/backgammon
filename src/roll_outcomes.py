# -*- coding: utf-8 -*-
from helpers.frequencies import compute_frequencies

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

# Call helper function to generate dict for frequencies of each possible roll
frequencies_dict = compute_frequencies(possible_rolls)


# Generate a dictionary of probabilities for each move option from count_dict
probs_dict = {}

print(*possible_rolls, sep="\n")
print("")
print(frequencies_dict)
