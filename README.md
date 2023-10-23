# Backgammon

**Overview**

Backgammon is a dice-based boardgame, the roots of which date back as many as 5,000 years ([Wikipedia](https://en.wikipedia.org/wiki/Backgammon)) to table games originating in Mesopotamia and Persia.

The use of dice in backgammon presents questions of discrete probability, and also a simple scenario for experimenting with data analysis and visualisation.

The rule on rolling doubles, and the feature of being able to take the face value of each die alone or in combination (see below), make this a (marginally) more interesting subject than typical probability calculations for two six-sided dice.

**Basic rules**

Knowledge of the full rules of backgammon isn't necessary to follow this exercise, but one comprehensive version of the rules (with graphics) can be accessed [here](https://www.bkgm.com/rules.html).

For the purpose of this repo, relevant rules are as follows:

- Players roll two six-sided dice to determine the number of spaces they can move.

- Moves are made separately or in combination; for a roll of [4, 5] a player can move:

  - one piece 4 spaces and a second piece 5 spaces (or vice versa), or
  - one piece a total of 9 spaces.

- Players can move onto any space permitted by their dice roll, unless that space contains two or more of the opponent's pieces.

**Doubles**

Doubles (e.g., [5, 5]) permit four moves rather than two (i.e., [5, 5, 5, 5]), to be used in combination on between one and four pieces.

This makes it possible to reach 15, 16, 18, 20, and 24, but also skews the probabilities of reaching numbers between 1 and 12. For example, the roll [3, 3] grants the moves [3, 3, 3, 3], and could be used to move a single piece 3, 6, 9, or 12 spaces.

## Findings

This repo explores the probabilities of being able to:

1. move _n_ spaces, for each possible move _n_;
2. move either _m_ or _n_ spaces, for each pair of possible moves (_m_, _n_); and
3. move _n_ spaces, and not _k_ spaces, for each pair of possible obstacles and moves (_k_, _n_).

### For each possible move _n_, what is the probability of being able to move _n_ spaces?

Denoted P(_n_), this is the probability _P_ of being able to move a piece _n_ spaces, within the range of possible moves. Move _n_ is possible if either die shows _n_ as its face value, or if the dice values can be summed to _n_.

The bar graph below depicts _P(n)_.

<img src="src/images/moves_by_probability.png" alt="Chart of Backgammon Moves by Probability"
        width="600" height="450">

For example, the probability of being able to move 9 spaces is: P(9) = 5/36 ≈ 13.89%. In addition to the four standard dice outcomes that sum to 9, [3, 6], [4, 5], [5, 4], and [6, 3], there is an exta means via [3, 3], since this grants the moves [3, 3, 3, 3], and the player could apply three of those values to reach 9.

As detailed above, the doubles rule makes possible five additional moves beyond 12 spaces. These are achieved through combinations of the moves presented via double 4 ([4, 4, 4, 4], for 16), double 5 ([5, 5, 5, 5], for 15 or 20) and double 6 ([6, 6, 6, 6], for 18 or 24).

There is just a 1/36 chance of reaching each of the values 15, 16, 18, 20, and 24, since this is the probability of rolling any given double. Since, for example, 18 and 24 are both reached via double 6, the probability of **being able to** move that number of spaces is what is related here. Whether a player does opt for either is independent of the probability of being presented with those choices.

The option to separate the face values of each die presents a further departure from the standard probabilities that result from a simple sum of two dice values.

For example, the roll [6, 1] not only presents the outcome 7, but also 1 and 6 as separate outcomes that could be used for different moves.

This significantly increases the probabilities of achieving each of the numbers from 1 to 6, as compared with a simple sum of values - note that 1 has probability 0 when taking the sum of two dice values, since even the lowest outcome [1, 1] sums to 2, whereas here there is an 11/36 chance (≈ 30.56%) of being able to select 1 as an outcome.

Note that an implication of the separation of dice values is that the sum of probabilities for all of the 17 possible moves is greater than 1. This is a feature of the rule permitting selection between the two dice values or their sum when applied to moves; the probability of each of the 36 possible dice outcomes is still 1/36, and sums to exactly 1.

### For each pair of possible moves (_m_, _n_), what is the probability of being able to move **either** _m_ **or** _n_ spaces?

Denoted P(_m_ or _n_), this is the probability _P_ of being able to move either a piece either _m_ or _n_ spaces, within the range of possible moves.

The probability is calculated as: P(_m_ or _n_) = P(_m_) + P(_n_) - P(_m_ and _n_).

Since we are concerned with the probability that either _m_ or _n_ is achieved, the probability that both occur is subtracted so as to avoid double-counting.

For example, take _m_ = 5, and _n_ = 7. A roll of [5, 2] could be used to satisfy either 5 or 7, but it is just one roll outcome, and so should be counted only once. By the same rationale, if n = 2 and we roll a double 2 for [2, 2, 2, 2], this is also one outcome that satisfies the condition, regardless of the fact that there exist four different ways to select 2 from [2, 2, 2, 2].

The heatmap below depicts P(_m_ or _n_).

<img src="src/images/combined_probability.png" alt="Chart of Backgammon Move Pairs by Combined Probability"
        width="600" height="450">

For example, for m = 4 and n = 12 the probability of being able to move either 4 or 12 spaces is: P(4 or 12) = 17/36 ≈ 47.22%.

In the bar graph above, the individual probabilities were P(4) = 15/36, and P(12) = 3/36. There exists one instance of overlap in which both 4 and 12 can be achieved: a double 4 for [4, 4, 4, 4].

Therefore, P(4 or 12) = P(4) + P(12) - P(4 and 12) = 15/36 + 3/36 - 1/36 = 17/36 ≈ 47.22%.

Compared with the single P(_n_) case, probabilities under the P(_m_ or _n_) case exhibit the most significant increases for the face values of the dice (from 1 to 6), followed by move pairs involving sums of the dice (from 7 to 12).

Beyond those values, since the values 15, 16, 18, 20, and 24 can only be achieved via doubles, (_m_, _n_) pairs involving these values see either a marginal or no probability increase compared with the standalone case.

To illustrate, 16 can only be achieved through a double 4, for [4, 4, 4, 4]. 16 is contingent on a subset of outcomes that achieve 4, and so P(4 or 16) = P(4) = 15/36.

Likewise, the outcome 24 is contingent on rolling double 6, for [6, 6, 6, 6]. Pairing this _m_ with any _n_ that is not a multiple of 6, becomes a strict either or case with no overlap.

For _m_ = 24, _n_ = 7: P(24 or 7) = 1/36 + 6/36 - 0/36 = 7/36 ≈ 19.44%.

### For each possible move _n_, what is the probability of being able to move _n_ spaces under the constraint of _k_ obstacles?

P(_n_ not _k_)

_More coming soon._
