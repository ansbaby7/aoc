f = open("../input.txt")
data = f.read().rstrip()


# data = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

for i in range(13, len(data)):
    s = set()
    for c in data[i-13:i+1]:
        s.add(c)
    if len(s) == 14:
        print(i+1)
        break