with open("day_06/input.txt", "r") as f:
    datastream = f.read().strip()

##########
# Part 1 #
##########

# How many characters need to be processed before the first start-of-packet marker is detected?
# + for index starting at 0, + 3 for first three windows smaller than 4 we dont count with our slicing
print(f"Part 1: {[len(set(datastream[i: i + 4])) for i in range(len(datastream))].index(4) + 1 + 3}")

##########
# Part 2 #
##########

# Same as above but window size 14, add 1 for index starting at 0, add 13 to account for missing windows
print(f"Part 2: {[len(set(datastream[i: i + 14])) for i in range(len(datastream))].index(14) + 1 + 13}")
