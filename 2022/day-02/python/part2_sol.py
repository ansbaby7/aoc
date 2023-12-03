f = open("../input.txt")
data = f.read()
strategy = [i.split(" ") for i in data.split("\n")]
# print(strategy)

score = 0


for s in strategy:
    result = (ord(s[1]) - 87)%3
    opponent = (ord(s[0]) - 64)%3
    player = (result + opponent)%3
    score += (ord(s[1]) - 88)*3 + player + 1

print(score)
