from math import prod

with open("day_08/input.txt", "r") as f:
    grid = [[int(i) for i in line.strip()] for line in f.readlines()]

##########
# Part 1 #
##########

h = len(grid)
w = len(grid[0])
visible = 0

# Consider your map; how many trees are visible from outside the grid?
for y in range(h):
    for x in range(w):
        cur = grid[y][x]
        if y == 0 or y == h - 1 or x == 0 or x == w - 1:
            visible += 1
        #    row left of current cell  row right of current cell     column above current cell                       column below current cell
        elif max(grid[y][:x]) < cur or max(grid[y][x + 1:]) < cur or max([grid[i][x] for i in range(0, y)]) < cur or max([grid[i][x] for i in range(y + 1, h)]) < cur:
            visible += 1
        else:
            pass

print(f"Part 1: {visible}")

##########
# Part 2 #
##########

def cut_list(l: list, limit: int) -> list:
    """ Trims list to only contain all values before a value lower than limit"""

    for i, v in enumerate(l):
        if v >= limit:
            return l[:i + 1]
    return l

max_score = 0

# Consider each tree on your map. What is the highest scenic score possible for any tree?
for y in range(h):
    for x in range(w):
        cur = grid[y][x]

        # Reverse lists left and above current cell so the order is the one
        # you see from the current tree
        l = cut_list(grid[y][:x][::-1], cur)
        r = cut_list(grid[y][x + 1:], cur)
        u = cut_list([grid[i][x] for i in range(0, y)][::-1], cur)
        d = cut_list([grid[i][x] for i in range(y + 1, h)], cur)
        score = prod([len(l_) for l_ in [l, r, u, d]])
        if score > max_score:
            max_score = score

print(f"Part 2: {max_score}")
