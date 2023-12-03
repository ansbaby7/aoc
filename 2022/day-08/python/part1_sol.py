f = open("../input.txt")
data = f.read().strip()
f.close()

grid = data.split("\n")
# print(grid)
l = len(grid)
visible = [[-1]*l for i in range(l)]
count = 0

for k in range(l):
    left_max, right_max= -1, -1
    i, j = 0, l-1
    while i < l:
        val = int(grid[k][i])
        if val > left_max:
            left_max = val
            if visible[k][i] == -1:
                count += 1
                visible[k][i] = val
        val = int(grid[k][j])
        if val > right_max:
            right_max = val
            if visible[k][j] == -1:
                count += 1
                visible[k][j] = val
        i += 1
        j -= 1
# print(visible)

for k in range(l):
    up_max, down_max= -1, -1
    i, j = 0, l-1
    while i < l:
        val = int(grid[i][k])
        if val > up_max:
            up_max = val
            if visible[i][k] == -1:
                    count += 1
                    visible[i][k] = val
        val = int(grid[j][k])
        if val > down_max:
            down_max = val
            if visible[j][k] == -1:
                count += 1
                visible[j][k] = val
        i += 1
        j -= 1

# print(visible)
print(count)

            

