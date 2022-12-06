with open("day_04/input.txt", "r") as f:
    # Transforms strings like 22-77,14-96 to lists like [[22, 77], [14, 96]]
    input_ = [[[int(i) for i in ids.split("-")] for ids in line.strip().split(",")] for line in f.readlines()]

##########
# Part 1 #
##########

# In how many assignment pairs does one range fully contain the other?
#                      right pair contained in left pair                      left pair contained in right pair
print(f"Part 1: {sum([(ids[0][0] <= ids[1][0] and ids[0][1] >= ids[1][1]) or (ids[0][0] >= ids[1][0] and ids[0][1] <= ids[1][1]) for ids in input_])}")

##########
# Part 2 #
##########

# In how many assignment pairs do the ranges overlap?
print(f"Part 2: {sum([(group[1][0] <= group[0][1] and group[1][0] >= group[0][0]) or (group[0][0] <= group[1][1] and group[0][0] >= group[1][0]) for group in input_])}")
