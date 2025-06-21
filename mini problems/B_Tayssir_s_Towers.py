from collections import Counter
n=int(input())
bar=list(map(int, input().split()))
count=Counter(bar)
max_hei=max(count.values())
num_towers=len(count)
print(max_hei, num_towers)
