f = open("../input.txt")
data = f.read()

rucksacks = data.split("\n")

sum = 0
for i in range(0, len(rucksacks), 3):
    for item in rucksacks[i]:
        if (item in rucksacks[i+1] and item in rucksacks[i+2]):
            if ord(item) >= 97:
                sum += ord(item) - 96
            else:
                sum += ord(item) - 64 + 26
            break

print(sum)