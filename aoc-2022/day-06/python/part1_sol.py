f = open("../input.txt")
data = f.read().rstrip()


# data = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

for i in range(3, len(data)):
    s = set()
    for c in data[i-3:i+1]:
        s.add(c)
    if len(s) == 4:
        print(i+1)
        break