# -*- coding: utf-8 -*-

def compute_rolls(num_sides=6, num_dice=2) -> list:
    """
    num_sides: an int of the number of sides each die has
    num_dice: an int of the number of dice - not currently in use
    Returns a list of lists representing the possible outcomes of rolling 
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
        print("Please enter an integer > 1 and try again.")
