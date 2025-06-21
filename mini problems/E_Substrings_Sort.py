n = int(input())
strings = [input().strip() for _ in range(n)]
strings.sort(key=len)


valid = True
for i in range(n - 1):
    if strings[i] not in strings[i + 1]:
        valid = False
        break

if valid:
    print("YES")
    for s in strings:
        print(s)
else:
    print("NO")
