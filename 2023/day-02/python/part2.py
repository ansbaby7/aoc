# with open('../sample.txt') as file:
with open('../input.txt') as file:
    lines = file.readlines()

ans = 0
for line in lines:
    split1 = line.strip().split(":")
    id = split1[0].split()[1]
    split2 = split1[1].split(";")
    # print(split2)
    max_r, max_g, max_b = 0, 0, 0
    for set in split2:
        split3 = set.split(",")
        for cube in split3:
            split4 = cube.split()
            # print(split4)
            val = int(split4[0])
            if split4[1] == 'red':
                if val > max_r:
                    max_r = val
            if split4[1] == 'green':
                if val > max_g:
                    max_g = val
            if split4[1] == 'blue':
                if val > max_b:
                    max_b = val
    # if max_r == 0 or max_g == 0 or max_b == 0:
    #     print(id)
    ans += (max_r * max_g * max_b)

# print(lines[-1])
print(ans)