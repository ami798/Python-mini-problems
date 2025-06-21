t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    words = [input().strip() for _ in range(n)]
    
    total = 0
    count = 0
    for word in words:
        if total + len(word) <= m:
            total += len(word)
            count += 1
        else:
            break
    print(count)
