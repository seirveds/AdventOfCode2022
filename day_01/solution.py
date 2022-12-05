with open("day_01/input.txt", "r") as f:
    input_ = [[int(i) for i in group.split("\n") if i] for group in f.read().split("\n\n")]

##########
# Part 1 #
##########

# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
print(f"Part 1: {max([sum(group) for group in input_])}")

##########
# Part 2 #
##########

# Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
print(f"Part 2: {sum(sorted([sum(group) for group in input_])[-3:])}")
