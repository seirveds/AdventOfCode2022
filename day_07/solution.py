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
            
print(f"Part 1: {sum([v for v in dir_sizes.values() if v <= 100000])}")

##########
# Part 2 #
##########
