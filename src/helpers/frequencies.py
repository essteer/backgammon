# -*- coding: utf-8 -*-
from helpers.powerset import powerset


def compute_frequencies(possible_rolls) -> list:
    """
    possible_rolls: list of lists of integers, containing possible outcomes from two fair six-sided dice
    Calls the itertools powerset function to generate a powerset of those outcomes
    Calculates the sum of each non-blank subset, representing possible move choices
    Returns a dictionary of:
    - key: an integer that can be reached from at least 1 roll combination
    - value: an integer of the number of combinations that can result in the key integer 
    """
    # Create empty dict to store counts of each move option
    frequency_dict = {}
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
                # Iterate value by 1
                frequency_dict[choice] += 1
            except KeyError:
                # Create new key, value pair if key not found
                frequency_dict[choice] = 1

    return frequency_dict
