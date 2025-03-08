num = int(input().strip())
for _ in range(num):
    n = int(input().strip())
    h = 0
    for i in range(1, (n // 2) + 1):
        h += i * 8 * i
    print(h)
