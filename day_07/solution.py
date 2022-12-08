from collections import defaultdict

with open("day_07/input.txt", "r") as f:
    command_log = [line.strip() for line in f.readlines()]

##########
# Part 1 #
##########

dir_sizes = defaultdict(int)
curr_dir = []

for line in command_log:
    if line.startswith("$ cd"):
        if line.endswith(".."):
            curr_dir.pop(-1)
        else:
            curr_dir.append(line.split(" ")[-1] + "/")
    elif line == "$ ls" or line.startswith("dir"):
        pass
    else:
        size, _ = line.split(" ")
        # Update size of directory and all parent directories
        for i in range(len(curr_dir)):
            dir_sizes["".join(curr_dir[:i + 1])] += int(size)

# Find all of the directories with a total size of at most 100000.
# What is the sum of the total sizes of those directories?         
print(f"Part 1: {sum([v for v in dir_sizes.values() if v <= 100000])}")

##########
# Part 2 #
##########

# Find the smallest directory that, if deleted, would free up enough space on the filesystem
# to run the update. What is the total size of that directory?

# Smallest directory with a size larger than what is needed to free up more than 30.000.000 storage space
print(f"Part 2: {sorted([v for v in dir_sizes.values() if v >= 30_000_000 - (70_000_000 - dir_sizes['//'])])[0]}")
