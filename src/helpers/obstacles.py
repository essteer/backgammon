# -*- coding: utf-8 -*-
from helpers.combinations import combination_moves


def add_obstacles(possible_rolls: list, distance_1: int, distance_2: int = 0, obstacles: list = []):
    """
    Takes a list of possible dice roll outcomes, possible_rolls
    and two integers, distance_1 and distance_2, 

    "adds" obstacles by removing combinations from possible_rolls that
    would depend on landing on a blocked space
    e.g., for a target space 7 spaces away, and an obstacle 4 spaces away,
    [5,2] and [1,6] are possible, but [4,3] and [3,4] are not

    calls combination_moves() on the updated list
    returns the number of combinations that result in the target number of spaces
    without use of obstructed spaces

    Args:
        possible_rolls: list of lists of integers, possible outcomes from rolls of two six-sided dice
        distance_1: an integer 1 <= x <= 24 describing the first of the target numbers
        distance_2: an integer 1 <= x <= 24 describing the second of the target numbers
        obstacles: list of integers, spaces with obstacles that cannot be landed on
    Returns:
        an integer, the number of rolls that permit distance_1 and/or distance_2 moves
        under the constraint of obstacles
    """
    try:
        targets = [int(distance_1), int(distance_2)]
    except TypeError:
        print("Error - distances must be integers: 1 <= x <= 24.")

    if len(obstacles) == 0:
        print("No obstacles present.")
        # TODO first write based on 1 target only
        combination_frequencies = combination_moves(
            unobstructed_rolls, distance_1)

        return combination_frequencies

    else:
        try:
            obstacle_check = [int(obstacle) for obstacle in obstacles]
        except TypeError:
            print("Error - obstacles must be integers: 1 <= x <= 24.")

    if targets[0] in obstacles:
        print(f"Target space {targets[0]} is obstructed.")
        return 0

    unobstructed_rolls = []

    for roll in possible_rolls[:]:

        for i in range(len(roll)):
            # Remove option for obstructed spaces from individual dice
            # TODO update this to prevent e.g. 2 being moved if other die value moved first
            if roll[i] in obstacles:
                roll[i] = 0

        if sum(roll) == targets[0]:
            continue

        else:
            unobstructed_rolls.append(roll)

    # TODO first write based on 1 target only
    # if distance_2 == False:
    #     combination_frequencies = combination_moves(
    #         unobstructed_rolls, distance_1)

    combination_frequencies = combination_moves(
        unobstructed_rolls, distance_1, distance_2)

    return combination_frequencies
