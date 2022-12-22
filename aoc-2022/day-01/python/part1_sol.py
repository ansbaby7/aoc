f = open("../input.txt")

text = f.read().split("\n")
f.close()

max = 0


calories = 0
for val in text:
    if val == '':
        if calories > max:
            max = calories
        calories = 0
    else:
        calories += int(val)

print(max)