with open("day_10/input.txt", "r") as f:
    cpu_ins = f.read().strip()
    # Pad addx with noop instructions so the "during cycle" part
    # is easily skipped
    cpu_ins = cpu_ins.replace("addx", "noop\naddx")
    cpu_ins = cpu_ins.split("\n")

##########
# Part 1 #
##########

# Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles.
# What is the sum of these six signal strengths?
x = 1
signal_strengths = []
for cycle, ins in enumerate(cpu_ins, start=1):
    # During cycle
    if cycle in [20, 60, 100, 140, 180, 220]:
        signal_strengths.append(x * cycle)
    # End of cycle
    if ins != "noop":
        x += int(ins.split()[-1])

print(f"Part 1: {sum(signal_strengths)}")

##########
# Part 2 #
##########

screen = ""

x = 1
for cycle, ins in enumerate(cpu_ins, start=1):
    # During cycle
    if (cycle % 40) - 1 in range(x-1, x + 2):
        screen += "▮"
    else:
        screen += " "

    # End of cycle
    if ins != "noop":
        x += int(ins.split()[-1])
nl = "\n"
print(f"Part 2:\n{nl.join([''.join(screen[tup[0]: tup[1]]) for tup in [(i, i+41) for i in range(0, 201, 40)]])}")
