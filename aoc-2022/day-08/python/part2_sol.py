f = open("input.txt")
data = f.read().strip()
f.close()

# grid = [[int(i) for i in s] for s in data.split("\n")]
grid = data.split("\n")
# print(grid)
l = len(grid)

max_score = 0
for i in range(1, l-1):
    for j in range(1, l-1):
        left = list(reversed(grid[i][0:j]))
        right = grid[i][j+1:l]
        top = [grid[i-k][j] for k in range(1, i+1)]
        down = [grid[i+k][j] for k in range(1, l-i)]

        score = 1
        for side in [left, right, top, down]:
            count = 0
            for height in side:
                count += 1
                if height >= grid[i][j]:
                    break
            score *= count
        if score > max_score:
            max_score = score
    
print(max_score)