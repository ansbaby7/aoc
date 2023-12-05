# with open('../sample.txt', 'r') as file:
with open('../input.txt', 'r') as file:
    lines = file.readlines()

l = len(lines)
star_positions = []
number_positions = []

for i, line in enumerate(lines):
    line = line.strip()
    n = len(line)
    positions = []
    j = 0
    while j < n:
    # for j, ch in enumerate(line):
        ch = line[j]
        if ch == '*':
            star_positions.append((i, j))
            j += 1
        elif ch.isdigit():
            startix = j
            while j < n and line[j].isdigit():
                j += 1
            endix = j - 1
            val = int(line[startix:endix + 1])
            positions.append((startix, endix, val))
        else:
            j += 1
    number_positions.append(positions)

# print(number_positions)
# print(star_positions)

ans = 0
for i, j in star_positions:
    possible_numbers = number_positions[i][:]
    if i > 0:
        possible_numbers += number_positions[i-1]
    if i < l - 1:
        possible_numbers += number_positions[i + 1]
    # print(possible_numbers)
    count = 0
    gear_ratio = 1
    for start, end, val in possible_numbers:
        if j >= start - 1 and j <= end + 1:
            count += 1
            gear_ratio *= val
    if count == 2:
        ans += gear_ratio

print(ans)



