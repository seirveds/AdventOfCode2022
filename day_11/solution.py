with open("day_11/input.txt", "r") as f:
    monkey_input = [[line.strip() for line in group.split("\n")] for group in f.read().split("\n\n")]


class Monkey:

    def __init__(self, definition):
        self.items = None
        self.operation = None
        self.divisible = None
        self.test_true = None
        self.test_false = None
        self.inspections = 0

        self.parse_definition(definition)

    def parse_definition(self, definition):
        self.items = [int(num.strip()) for num in definition[1].replace("Starting items:", "").split(",")]
        self.operation = definition[2].split(" = ")[-1]
        self.divisible = int(definition[3].split(" ")[-1])
        self.test_true = int(definition[4].split(" ")[-1])
        self.test_false = int(definition[5].split(" ")[-1])

    def inspect_items(self, part1=True):
        global monkeys
        for old in self.items:
            self.inspections += 1
            new = eval(self.operation)
            if part1:
                new = new // 3
            if new % self.divisible == 0:
                monkeys[self.test_true].items.append(new)
            else:
                monkeys[self.test_false].items.append(new)
        self.items = []


##########
# Part 1 #
##########

monkeys = [Monkey(m) for m in monkey_input]

for _ in range(20):
    for m in monkeys:
        m.inspect_items(part1=True)

# What is the level of monkey business after 20 rounds of stuff-slinging simian shenanigans?
ins = sorted([m.inspections for m in monkeys])
print(f"Part 1: {ins[-2] * ins[-1]}")
