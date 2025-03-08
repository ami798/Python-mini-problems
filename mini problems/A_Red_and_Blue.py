t = int(input())

for _ in range(t):
    n = int(input())
    col = list(map(int, input().split()))
    col.sort()
    blue_col = col[0]
    red_col = 0

    left = 1
    right = n - 1

    while left < right:
        blue_col += col[left]
        red_col += col[right]

        if red_col > blue_col:
            break

        left += 1
        right -= 1

    if red_col > blue_col:
        print("YES")
    else:
        print("NO")