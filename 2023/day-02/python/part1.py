# with open('../sample.txt') as file:
with open('../input.txt') as file:
    lines = file.readlines()

ans = 0
for line in lines:
    f = 0
    split1 = line.strip().split(":")
    id = split1[0].split()[1]
    split2 = split1[1].split(";")
    # print(split2)
    for set in split2:
        split3 = set.split(",")
        for cube in split3:
            split4 = cube.split()
            # print(split4)
            if split4[1] == 'red':
                if int(split4[0]) > 12:
                    f = 1
            if split4[1] == 'green':
                if int(split4[0]) > 13:
                    f = 1
            if split4[1] == 'blue':
                if int(split4[0]) > 14:
                    f = 1
    if f == 0:
        # print(line)
        # print(id)
        ans += int(id)

# print(lines[-1])
print(ans)