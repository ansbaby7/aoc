f = open("../input.txt")
data = f.read().strip()

pairs = data.split("\n")

count = 0
for pair in pairs:
    ranges = pair.split(",")
    l1, r1 = ranges[0].split("-")
    l2, r2 = ranges[1].split("-")
    l1, r1, l2, r2 = int(l1), int(r1), int(l2), int(r2) 
    if (r1 < l2) or (r2 < l1):
        continue
    else:
        count += 1

print(count)