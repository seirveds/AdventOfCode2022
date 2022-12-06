with open("day_04/input.txt", "r") as f:
    # Transforms strings like 22-77,14-96 to lists like [[22, 77], [14, 96]]
    input_ = [[[int(i) for i in ids.split("-")] for ids in line.strip().split(",")] for line in f.readlines()]

##########
# Part 1 #
##########

print(f"Part 1: {sum([(ids[0][0] <= ids[1][0] and ids[0][1] >= ids[1][1]) or (ids[0][0] >= ids[1][0] and ids[0][1] <= ids[1][1]) for ids in input_])}")

