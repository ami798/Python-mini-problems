n = int(input())
cards = [int(input()) for _ in range(n)]
frequency = {}
for card in cards:
    if card in frequency:
        frequency[card] += 1
    else:
        frequency[card] = 1
values = list(frequency.values())
if len(values) == 2 and values[0] == values[1]:
    distinct_numbers = list(frequency.keys())
    print("YES")
    print(distinct_numbers[0], distinct_numbers[1])
else:
    print("NO")