# -*- coding: utf-8 -*-

def compute_rolls(num_sides=6) -> list:
    """
    Takes an integer num_sides for the number of sides for two fair dice
    adds possible roll combinations to a list
    marks doubles e.g., [3, 3] as choices of [3, 3, 3, 3] in line with backgammon rules
    returns a list of possible roll combinations

    Args:
        num_sides: an integer of the number of sides each die has
    Returns:
        a list of lists representing the possible outcomes of rolling
        num_dice dice with num_sides sides each
    """
    # Ensure an int is passed or convert a float
    try:
        dice_range = int(num_sides + 1)

        possible_rolls = []

        # Generate possible outcomes from rolling num_dice fair num_sides-sided dice
        for i in range(1, dice_range):
            for j in range(1, dice_range):
                if i == j:
                    # Backgammon rules: doubles yield four moves
                    # E.g. rolling [3, 3] gives a player the move options [3, 3, 3, 3]
                    possible_rolls.append([i]*4)
                else:
                    possible_rolls.append([i, j])

        return possible_rolls

    except TypeError:
        print("Please enter an integer 1 <= x <= 24 and try again.")
