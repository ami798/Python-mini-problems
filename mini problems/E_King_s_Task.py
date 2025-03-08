from collections import deque

def swap1(p):
    n = len(p) // 2
    for i in range(n):
        p[2 * i], p[2 * i + 1] = p[2 * i + 1], p[2 * i]
    return p

def swap2(p):
    n = len(p) // 2
    for i in range(n):
        p[i], p[n + i] = p[n + i], p[i]
    return p

n = int(input().strip())
p = list(map(int, input().strip().split()))

s_p = list(range(1, 2 * n + 1))
v = set()
q = deque([(p, 0)])

while q:
    cur, st = q.popleft()
    if cur == s_p:
        print(st)
        break
    if tuple(cur) in v:
        continue
    v.add(tuple(cur))
    q.append((swap1(cur.copy()), st + 1))
    q.append((swap2(cur.copy()), st + 1))
else:
    print(-1)
