# -*- coding: utf-8 -*-
from helpers.combinations import combination_moves


def add_obstacles(possible_rolls: list[list[int]],
                  distance_1: int,
                  distance_2: int = 0,
                  obstacles: list[int] = []) -> int:
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
        combination_frequencies = combination_moves(
            filtered_rolls, distance_1)

        return combination_frequencies

    else:
        try:
            obstacle_check = [int(obstacle) for obstacle in obstacles]
        except TypeError:
            print("Error - obstacles must be integers: 1 <= x <= 24.")

    for i in range(len(targets)):
        # Check whether target spaces are obstructed
        if targets[i] in obstacles:
            print(f"Target space {targets[i]} is obstructed.")
            return 0

    # Call helper function filter_rolls
    filtered_rolls = filter_rolls(possible_rolls[:], obstacles[:])

    # Send filtered_rolls list to combination_moves function
    combination_frequencies = combination_moves(
        filtered_rolls, distance_1, distance_2)

    return combination_frequencies


def filter_rolls(possible_rolls: list[list[int]], obstacles: list[int]) -> list[list[int]]:
    """
    Helper function for add_rolls - takes possible_rolls and obstacles lists
    and filters out obstructed moves

    Args:
        possible_rolls: list of lists of integers, possible outcomes from rolls of two six-sided dice
        obstacles: list of integers, spaces with obstacles that cannot be landed on
    Returns:
        list of rolls modified to remove obstructed rolls
    """

    def is_valid_roll(roll: list[int]) -> bool:
        """
        Checks whether the moves in a roll are possible.
        E.g., with obstacles on spaces [4, 6], a roll of:
            [6, 4] is not viable because neither move can be made, but
            [4, 5] is viable because 5 can be played first, and then 4 from the 5 space
        Returns:
            True if roll is not a subset of obstacles
            False if roll is subset of obstacles (i.e. all moves are obstructed)
        """
        return not set(roll[:]).issubset(obstacles)

    def process_doubles(doubles: list[list[int]]) -> list[list[int]]:
        """
        Doubles [3, 3] grant four moves by default [3, 3, 3, 3],
        but if e.g. space 9 is blocked, [3, 3, 3, 3] becomes [3, 3], 
        since the 3rd and 4th 3s are inaccessible

        Returns:
            List of doubles modified to remove obstructed moves
        """
        output = []
        for roll in doubles:
            if roll[0]*2 in obstacles:
                output.append(roll[:1])
            elif roll[0]*3 in obstacles:
                output.append(roll[:2])
            elif roll[0]*4 in obstacles:
                output.append(roll[:3])
            else:
                output.append(roll)

        return output

    # Remove rolls that are completely obstructed
    filtered_rolls = list(filter(is_valid_roll, possible_rolls))
    # Separate regular rolls and doubles
    non_doubles = [roll for roll in filtered_rolls if len(roll) == 2]
    doubles = [roll for roll in filtered_rolls if len(roll) != 2]
    # If there are no valid doubles remaining, return regular rolls only
    if doubles == []:
        return non_doubles
    # Process any remaining doubles to strip out inaccessible moves
    processed_doubles = process_doubles(doubles)

    return non_doubles + processed_doubles
