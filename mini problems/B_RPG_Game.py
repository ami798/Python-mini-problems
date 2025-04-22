s, n = map(int, input().split())
dragons = [tuple(map(int, input().split())) for _ in range(n)]
dragons.sort()

for strength, bonus in dragons:
    if s > strength:
        s += bonus
    else:
        print("NO")
        break
else:
    print("YES")
