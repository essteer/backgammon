# -*- coding: utf-8 -*-

def combination_moves(possible_rolls, distance_1, distance_2=0) -> int:
    """
    Takes a list of possible dice roll outcomes, possible_rolls
    and two integers, distance_1 and distance_2, 
    iterates through possible_rolls to count combinations that result in either or both targets
    does not double-count a roll outcome that could satisfy both moves
    returns the number of combinations that result in either or 
    both of those integers through combinations of two dice rolls.

    Args:
        possible_rolls: list of lists of integers, possible outcomes from rolls of two six-sided dice
        distance_1: an integer 1 <= x <= 24 describing the first of the target numbers
        distance_2: an integer 1 <= x <= 24 describing the second of the target numbers
    Returns:
        an integer, the number of rolls that permit distance_1 and/or distance_2 moves
    """
    try:
        targets = [int(distance_1), int(distance_2)]
    except TypeError:
        print("Error - distances must be integers: 1 <= x <= 24.")

    total = 0

    for roll in possible_rolls[:]:

        if len(roll) != 2:
            # a double roll has len() == 4 (e.g. [3,3] -> [3,3,3,3])
            # separate out double rolls to capture extended move combinations
            # e.g., [5,5] becomes [5,5,5,5] with the option of moving a piece 5, 10, 15 or 20 spaces
            combinations = [roll[0]*(i+1) for i in range(len(roll))]
            # increase the total count if a target distance can be reached
            if targets[0] in combinations or targets[1] in combinations:
                total += 1
        # increase the total count if a target distance can be reached
        elif targets[0] in roll or targets[1] in roll or sum(roll) in targets:
            total += 1

    return total
