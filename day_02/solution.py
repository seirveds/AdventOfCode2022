# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors

# The score for a single round is the score for the shape you selected
# (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round
# (0 if you lost, 3 if the round was a draw, and 6 if you won).
    

with open("day_02/input.txt", "r") as f:
    input_ = [line.strip() for line in f.readlines()]

def score(strategy: str) -> int:
    """ Weird, complex way of calculating game score"""
    theirs, mine = strategy.split(" ")

    choice_score = dict(X=1, Y=2, Z=3)
    choice_points = choice_score[mine]

    # Turn X into A, Y into B, etc
    # Turn into ascii codes for easy comparison
    mine = ord(mine) - 23
    theirs = ord(theirs)

    # Same choice results in 0
    if mine - theirs == 0:
        result_score = 3
    # All winning results are either 1 or -2
    elif mine - theirs in [1, -2]:
        result_score = 6
    # All losing results are either -1 or 2
    elif mine - theirs in [-1, 2]:
        result_score = 0

    return choice_points + result_score

# Simple lookup dict
game_scores = {
    "A X": 1 + 3,
    "B Y": 2 + 3,
    "C Z": 3 + 3,
    "A Y": 2 + 6,
    "B Z": 3 + 6,
    "C X": 1 + 6,
    "A Z": 3 + 0,
    "B X": 1 + 0,
    "C Y": 2 + 0
}

##########
# Part 1 #
##########

# What would your total score be if everything goes exactly according to your strategy guide?
print(f"Part 1 (lookup dict): {sum([game_scores[line] for line in input_])}")
print(f"Part 1 (ascii codes): {sum([score(line) for line in input_])}")

##########
# Part 2 #
##########

# X means you need to lose,
# Y means you need to end the round in a draw,
# and Z means you need to win.

updated_game_scores = {
    "A X": 3 + 0,
    "B Y": 2 + 3,
    "C Z": 1 + 6,
    "A Y": 1 + 3,
    "B Z": 3 + 6,
    "C X": 2 + 0,
    "A Z": 2 + 6,
    "B X": 1 + 0,
    "C Y": 3 + 3
}

# Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?
print(f"Part 2: {sum([updated_game_scores[line] for line in input_])}")
