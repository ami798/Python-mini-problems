t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    l = n - k + 1
    r = n
    odd_count = (r + 1) // 2 - (l // 2)
    if odd_count % 2 == 0:
        print("YES")
    else:
        print("NO")
