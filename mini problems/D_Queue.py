n = int(input())
time = list(map(int, input().split()))
time.sort()

count = 0
current_time = 0

for t in time:
    if current_time <= t:
        count += 1
        current_time += t

print(count)