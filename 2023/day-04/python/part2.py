from collections import defaultdict

# with open("../sample.txt") as f:
with open("../input.txt") as f:
    lines = f.readlines()

card_map = defaultdict(int)
card_no = 1

for line in lines:
    line = line.strip()
    card_map[card_no] += 1
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
    card_copies = card_map[card_no]
    for i in range(1, win_count + 1):
        card_map[card_no + i] += 1 * card_copies
    card_no += 1
    
ans = 0
# print(card_map)
for card in card_map:
    ans += card_map[card]
print(ans)