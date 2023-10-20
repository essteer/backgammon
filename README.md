# Backgammon

**Overview**

The use of dice in backgammon presents questions of discrete probability, and also a simple scenario for experimenting with data analysis and visualisation.

The rule on rolling doubles, and the feature of being able to take the face value of each die alone or in combination (see below), make this a (marginally) more interesting subject than typical probability calculations for two six-sided dice.

**Background**

Backgammon is a boardgame, the roots of which date back as many as 5,000 years ([Wikipedia](https://en.wikipedia.org/wiki/Backgammon)) to table games originating in Mesopotamia and Persia.

The modern game involves two players alternating turns to roll two six-sided dice, the scores of which determine how many spaces each player may move their own pieces.

**Basic rules**

Knowledge of the full rules of backgammon isn't necessary to follow this exercise, but one typical version (with graphics) can be accessed [here](https://www.bkgm.com/rules.html).

For the purpose of this repo, relevant rules are as follows:

- Players roll two six-sided dice to determine the number of spaces they can move.

- Moves are made separately or in combination; for a roll of [4, 5] a player can move:

  - one piece 4 spaces and a second piece 5 spaces (or vice versa), or
  - one piece a total of 9 spaces.

- Players can move onto any space permitted by their dice roll, unless that space contains two or move of the opponent's pieces.

**Doubles**

Doubles (e.g., [5, 5]) permit four moves rather than two (i.e., [5, 5, 5, 5]), to be used in combination on between one and four pieces.

This makes it possible to reach 15, 16, 18, 20, and 24.

It also skews the probabilities of reaching the face value numbers between 1 and 12. For example, the roll [3, 3] grants the moves [3, 3, 3, 3], and could be used to move a single piece 3, 6, 9, or 12 spaces.

**About this repo**

Questions explored within this repo, include:

1. For each possible move _n_, what is the probability of being able to move _n_ spaces?

   <img src="src/images/moves_by_probability.png" alt="Chart of Backgammon Moves by Probability"
        width="600" height="450">

   _E.g., the probability of being able to move 9 spaces: P(9) = 5/36 ≈ 13.89%._

2. For each pair of possible moves (_m_, _n_), what is the probability of being able to move **either** _m_ **or** _n_ spaces?

   <img src="src/images/combined_probability.png" alt="Chart of Backgammon Move Pairs by Combined Probability"
        width="600" height="450">

   _E.g. the probability of being able to move either 4 or 12 spaces: P(4 or 12) = 17/36 ≈ 47.22%._

3. The probability of attacking an opponent's piece under movement constraints - i.e., where inbetween spaces are obstructed by two or more opposing pieces, and cannot be landed on.
