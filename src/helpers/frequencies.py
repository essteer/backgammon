# -*- coding: utf-8 -*-
from helpers.powerset import powerset


def compute_frequencies(possible_rolls: list[list[int]]) -> dict[int, int]:
    """
    Takes a list of possible dice roll outcomes, possible_rolls
    calls the itertools powerset function to generate a powerset of combinations from those rolls
    calculates the sum of each non-blank subset, 
    representing the frequency of each possible move choice, 1 <= x <= 24
    returns a dictionary mapping rolls to roll frequencies.

    Arg:
        possible_rolls: list of lists of integers, possible outcomes from rolls of two six-sided dice
    Returns a dictionary with:
        key: an integer that can be reached from at least 1 roll combination
        value: an integer of the number of combinations that can result in the key integer 
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
