n, k = map(int, input().split())
sweets = list(map(int, input().split()))

distributed = 0
remaining = 0

for day in range(1, n + 1):
   
    remaining += sweets[day - 1]
    
    give = min(remaining, 8)
    distributed += give
    remaining -= give

    if distributed >= k:
        print(day)
        break
else:

    print(-1)
