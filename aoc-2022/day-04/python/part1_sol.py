f = open("../input.txt")
data = f.read().strip()

pairs = data.split("\n")
# print(pairs)

count = 0
for pair in pairs:
    ranges = pair.split(",")
    l1, r1 = ranges[0].split("-")
    l2, r2 = ranges[1].split("-")
    l1, r1, l2, r2 = int(l1), int(r1), int(l2), int(r2) 
    if (l1 <= l2 and r1 >= r2) or (l1 >= l2 and r1 <= r2):
        count += 1

print(count)