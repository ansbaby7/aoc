f = open("../input.txt")
data = f.read()

rucksacks = data.split("\n")

sum = 0
for r in rucksacks:
    left = r[:len(r)//2]
    right = r[len(r)//2:]
    for item in left:
        if item in right:
            if ord(item) >= 97:
                sum += ord(item) - 96
            else:
                sum += ord(item) - 64 + 26
            break
print(sum)