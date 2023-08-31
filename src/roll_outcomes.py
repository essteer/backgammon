# -*- coding: utf-8 -*-
import random
from itertools import combinations, chain


possible_rolls = []

# Generate possible outcomes from rolling two dice
for i in range(1, 7):
    for j in range(1, 7):
        if i == j:
            possible_rolls.append([i]*4)
        else:
            possible_rolls.append([i, j])


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


# Create empty dict to store move probabilities
count_dict = {}
# Iterate through roll combinations and add occurrences to count_dict
for roll in possible_rolls:

    choices = []
    roll_combinations = powerset(roll)

    for x in roll_combinations:
        # Avoid double-counting:
        # e.g., a roll of two fours should permit the move 4 to be counted exactly once
        if sum(list(x)) not in choices:
            choices.append(sum(list(x)))

    for choice in choices[1:]:  # Skip blank subsets
        try:
            count_dict[choice] += 1
        except KeyError:
            count_dict[choice] = 1


# print(possible_rolls)
print("")
print(count_dict)
