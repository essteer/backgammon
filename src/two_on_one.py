# -*- coding: utf-8 -*-
from helpers.rolls import compute_rolls

# Call function to generate list of lists of possible roll outcomes
# Defaults to two six-sided dice
possible_rolls = compute_rolls()

# Set number of spaces needed to land a player's pieces on their opponent's piece:
distance_1 = 9  # later replace with input()
distance_2 = 16  # later replace with input()
targets = [distance_1, distance_2]

count = 0
for roll in possible_rolls:
    if len(roll) != 2:
        combinations = [roll[0]*(i+1) for i in range(len(roll))]
        if targets[0] in combinations or targets[1] in combinations:
            count += 1

    elif targets[0] in roll or targets[1] in roll or sum(roll) in targets:
        count += 1

print(
    f"Prob. able to land from either {distance_1} or {distance_2} spaces away: {100*(count/36):.2f}%")
