f = open("../input.txt")
data = f.read()

starting_stacks, rearrangement_steps = data.split("\n\n")
# print(starting_stacks)
# print(rearrangement_steps)

stack_rows = starting_stacks.split("\n")

# find no of stacks
num_stacks = len(list(filter(lambda x: x.isdigit(), stack_rows[-1].split(" "))))

map = {}
for i in range(num_stacks):
    map[i+1] = []

for i in reversed(range(len(stack_rows)-1)):
    for j in range(1, len(stack_rows[i]), 4):
        map[j//4 + 1].append(stack_rows[i][j])

for key in map:
    while map[key][-1] == " ":
        map[key].pop()

# print(map)

rearrangement_steps = rearrangement_steps.rstrip().split("\n")

for step in rearrangement_steps:
    num_items, from_, to = [int(c) for c in step.split(" ") if c.isdigit()]
    map[to] += list(reversed(map[from_]))[:num_items]
    map[from_] = map[from_][:-num_items]

for key in map:
    print(map[key][-1], end="")
