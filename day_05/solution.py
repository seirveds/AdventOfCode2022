from collections import defaultdict
from copy import deepcopy

with open("day_05/input.txt", "r") as f:
    # Replace instead of strip to keep leading whitespace
    input_ = [line.replace("\n", "") for line in f.readlines()]

# Parse crate positions
start_positions = input_[:8]  # 3

# Get column index and crate value for every row, starting at the bottom
parsed_start_positions = [[(i, c) for i, c in enumerate(line[1:-1:4], start=1)] for line in start_positions[::-1]]

# Transform crate positions to dict with column index as keys, and the stack of crates as list, with
# the first element being the bottom crate
state_dict = defaultdict(list)
for line in parsed_start_positions:
    for idx, crate in line:
        # Ignore empty spaces
        if crate != " ":
            state_dict[idx].append(crate)

# Parse moves
moves = input_[10:]  # 5

# Remove text from moves, only need numbers
moves = [[int(i) for i in line.split(" ")[1::2]] for line in moves]

##########
# Part 1 #
##########

state_dict_part_1 = deepcopy(state_dict)

# After the rearrangement procedure completes, what crate ends up on top of each stack?
for amount, from_, to in moves:
    to_move = state_dict_part_1[from_][-amount:]
    state_dict_part_1[from_] = state_dict_part_1[from_][:-amount]
    # Crates are moved one by one, so order is reversed
    state_dict_part_1[to].extend(to_move[::-1])
print(f"Part 1: {''.join([state_dict_part_1[k][-1] for k in state_dict_part_1])}")

##########
# Part 2 #
##########

state_dict_part_2 = deepcopy(state_dict)

# Same as above but without reversing the moved crate stack
for amount, from_, to in moves:
    to_move = state_dict_part_2[from_][-amount:]
    state_dict_part_2[from_] = state_dict_part_2[from_][:-amount]
    # Crates are now moved at once, no reversal needed
    state_dict_part_2[to].extend(to_move)

print(f"Part 2: {''.join([state_dict_part_2[k][-1] for k in state_dict_part_2])}")
