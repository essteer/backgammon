# -*- coding: utf-8 -*-


def compute_probabilities(frequency_dict) -> dict:
    """
    Takes frequency_dict, a dictionary of possible dice rolls and their frequency
    Returns a dictionary of:
    - key: same key integer as frequency_dict, an integer that can be reached from at least 1 roll combination
    - value: the probability of being able to reach the key integer with one roll of two fair six-sided dice, rounded to four decimal places
    """
    probability_dict = {k: round(v/36, 4) for k, v in frequency_dict.items()}

    return probability_dict
