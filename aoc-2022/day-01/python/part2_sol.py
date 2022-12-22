f = open("../input.txt")

text = f.read().split('\n')
f.close()
# print(text)

max1, max2, max3 = 0, 0, 0

calories = 0
for t in text:
    if t == '':
        # print(calories)
        if calories > max1:
            max3 = max2
            max2 = max1
            max1 = calories
        elif calories < max1 and calories > max2:
            max3 = max2
            max2 = calories
        elif calories < max2 and calories > max3:
            max3 = calories
        calories = 0
    else:
        calories += int(t)

# print(max1)
# print(max2)
# print(max3)
# calories = []
# calorie = 0

# for t in text:
#     if t == '':
#         calories.append(calorie)
#         calorie = 0
#     else:
#         calorie += int(t)

# print(calories)
# calories.sort()

# print(max(calories))
# print(calories[-1])
# print(calories[-2])
# print(calories[-3])

# print(calories[-1] + calories[-2] + calories[-3])



print(max1 + max2 + max3)



