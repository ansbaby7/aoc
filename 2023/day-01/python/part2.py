# with open("../sample2.txt") as f:
with open("../input.txt") as f:
    lines = f.readlines()

digits = list(map(str, range(1, 10)))
# print(digits)
digit_strings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

m = pow(10, 9) + 7
ans = 0

for line in lines:
    min_ix = m
    max_ix = -1
    d1 = 0
    d2 = 0
    for i, ds in enumerate(digit_strings):
        ix = line.find(ds)
        if ix != -1:
            if ix < min_ix:
                min_ix = ix
                d1 = i + 1
        ix = line.rfind(ds)
        if ix != -1:
            if ix > max_ix:
                max_ix = ix
                d2 = i + 1

    for i, ch in enumerate(line):
        if ch.isdigit():
            if i < min_ix:
                min_ix = i
                d1 = int(ch)
            
            if i > max_ix:
                max_ix = i
                d2 = int(ch)
    # print(d1, d2)
    ans += d1*10 + d2
    # print(ans)

print(ans)



