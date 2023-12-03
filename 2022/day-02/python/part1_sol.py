f = open("../input.txt")
data = f.read()
strategy = [i.split(" ") for i in data.split("\n")]
# print(strategy)

score = 0

for s in strategy:
    player = (ord(s[1]) - 87)%3
    opponent = (ord(s[0]) - 64)%3
    result = (player - opponent)%3
    if result == 1:
        points = 6
    elif result == 0:
        points = 3
    else:
        points = 0 
    score += ord(s[1]) - 87 + points

print(score)
