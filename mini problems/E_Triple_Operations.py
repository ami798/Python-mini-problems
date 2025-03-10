t = int(input().strip())
results = []

for _ in range(t):
    l, r = map(int, input().strip().split())
    steps = 0
    while r > 0:
        r //= 3
        steps += 1
    results.append(steps)

print("\n".join(map(str, results)))
