# -*- coding: utf-8 -*-


def compute_probabilities(frequency_dict: dict[int, int]) -> dict[int, float]:
    """
    Takes frequency_dict, a dictionary mapping roll combinations to roll frequencies
    calculates the probability of each roll 0 <= p < 1,
    as the proportion of 36 possible roll combinations from two fair six-sided dice
    that can result in a target integer 1 <= x <= 24 being achieved
    returns a dictionary mapping integers to probabilities

    Arg:
        frequency_dict: a dictionary mapping integers to roll frequencies
    Returns a dictionary with:
    - key: same key integer as frequency_dict, an integer that can be reached from at least 1 roll combination
    - value: probability of being able to reach the key integer with one roll of two fair six-sided dice, rounded to four decimal places
    """
    probability_dict = {k: round(v/36, 4) for k, v in frequency_dict.items()}

    return probability_dict
