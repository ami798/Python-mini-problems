t = int(input())
for _ in range(t):
    n = int(input())
    k = (n - 1) // 2
    result = 8 * k * (k + 1) * (2 * k + 1) // 6
    print(result)
