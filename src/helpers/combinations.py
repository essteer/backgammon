# -*- coding: utf-8 -*-

def combination_moves(possible_rolls, distance_1, distance_2=0) -> int:
    """
    possible_rolls: list of lists of integers, possible outcomes from two fair six-sided dice
    distance_1 and distance_2: integers 1 <= x <= 24 representing two move queries

    iterates through possible_rolls to count combinations that result in either or both moves

    does not double-count a roll outcome that could satisfy both moves

    Returns an integer, the number of rolls that permit distance_1 and/or distance_2 moves
    """

    targets = [distance_1, distance_2]
    total = 0

    for roll in possible_rolls:
        # a double roll results in four move options (e.g. [3,3] -> [3,3,3,3])
        # separate out double rolls to capture extended move combinations
        # e.g., [5,5] becomes [5,5,5,5] with the option of moving one piece 15 or 20 spaces
        if len(roll) != 2:
            combinations = [roll[0]*(i+1) for i in range(len(roll))]

            if targets[0] in combinations or targets[1] in combinations:
                total += 1

        elif targets[0] in roll or targets[1] in roll or sum(roll) in targets:
            total += 1

    return total
