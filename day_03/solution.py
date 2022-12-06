# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.

with open("day_03/input.txt", "r") as f:
    input_ = [line.strip() for line in f.readlines()]

priorities = {chr(c + 96): c  for c in range(1, 27)} | {chr(c + 38): c  for c in range(27, 53)}

##########
# Part 1 #
##########

# Split lines in half and make sets
backback_halves = [(set(l[:(len(l) // 2)]), set(l[(len(l) // 2):])) for l in input_]

# Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?
print(f"Part 1: {sum([sum([priorities[c] for c in tup[0] & tup[1]]) for tup in backback_halves])}")


##########
# Part 2 #
##########

# Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?
elf_groups = [[set(b) for b in input_[i: i + 3]] for i in range(0, len(input_), 3)]

print(f"Part 2: {sum([priorities[(group[0] & group[1] & group[2]).pop()] for group in elf_groups])}")
