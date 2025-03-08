def a(b):
    c = sum(d.count(1) for d in b)
    if c == 0:
        return 0
    elif c == 1 or c == 2:
        return 1
    else:
        return 2

e = int(input().strip())

for _ in range(e):
    f = [list(map(int, input().strip().split())) for _ in range(2)]
    g = a(f)
    print(g)
