n,m= map(int, input().split())
tasks = list(map(int, input().split()))

current = 1
total_time = 0

for task in tasks:
    if task >= current:
        total_time += task - current
    else:
        total_time += (n - current) + task
    current = task

print(total_time)