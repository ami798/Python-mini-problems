def f(a, b, c, d):
    x = abs(c - 1) + abs(d - 1)
    y = abs(c - 1) + abs(d - b)
    z = abs(c - a) + abs(d - 1)
    w = abs(c - a) + abs(d - b)
    return max(x, y, z, w)

t = int(input())
    x = abs(c - 1) + abs(d - 1)
    y = abs(c - 1) + abs(d - b)
    z = abs(c - a) + abs(d - 1)
    w = abs(c - a) + abs(d - b)

for _ in range(t):
    a, b, c, d = map(int, input().split())
    res = f(a, b, c, d)
    print(res)
