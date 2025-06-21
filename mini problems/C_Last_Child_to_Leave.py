n, m = map(int, input().split())
a = list(map(int, input().split()))
queue = []
for i in range(n):
    queue.append((i + 1, a[i])) 

last_child = -1
while queue:
    current = queue.pop(0)
    child_num, remaining = current
    if remaining > m:
        queue.append((child_num, remaining - m))
    else:
        last_child = child_num

print(last_child)