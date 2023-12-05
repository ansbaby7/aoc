# with open("../sample.txt") as f:
with open("../input.txt") as f:
    lines = f.readlines()

ans = 0
for line in lines:
    line = line.strip()
    split1 = line.split("|")
    split2 = split1[0].split(":")
    winning_numbers = split2[1].split()
    numbers_you_have = split1[1].split()
    # print(winning_numbers)
    # print(numbers_you_have)
    win_count = 0
    for num in numbers_you_have:
        if num in winning_numbers:
            win_count += 1
    if win_count > 0:
        ans += pow(2, win_count - 1)

print(ans)
