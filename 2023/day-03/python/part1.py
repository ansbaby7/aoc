# with open('../sample.txt', 'r') as file:
with open('../input.txt', 'r') as file:
    lines = file.readlines()

l = len(lines)
symbol_positions = []
for line in lines:
    line = line.strip()
    positions = []
    for i, ch in enumerate(line):
        if ch != '.' and (ch < '0' or ch > '9'):
            positions.append(i)
    symbol_positions.append(positions)

# print(symbol_positions)

ans = 0
for i, line in enumerate(lines):
    line = line.strip()
    j = 0
    n = len(line)

    possible_positions = symbol_positions[i][:]
    if i > 0:
        possible_positions += symbol_positions[i - 1]
    if i < l - 1:
        possible_positions += symbol_positions[i + 1]

    while j < n:
    # for j, ch in enumerate(line):
        ch = line[j]
        if ch.isdigit():
            startix = j
            while j < n and line[j].isdigit():
                j += 1
            endix = j - 1
            for ix in range(startix - 1, endix + 2):
                if ix in possible_positions:
                    val = int(line[startix:endix + 1])
                    # print(val)
                    ans += val
                    break
        else:
            j += 1

print(ans)