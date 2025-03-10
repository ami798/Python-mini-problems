t = int(input().strip())
results = []

for _ in range(t):
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    max_value = max(arr)
    score = max_value + (n + 1) // 2
    results.append(score)

print("\n".join(map(str, results)))
