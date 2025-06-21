t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    total = a + b + c

    if total % 3 != 0:
        print("NO")
    else:
        target = total // 3
        need_a = target - a
        need_b = target - b

        if need_a < 0 or need_b < 0:
            
            print("NO")
        elif need_a + need_b <= c:
            print("YES")
        else:
            print("NO")
