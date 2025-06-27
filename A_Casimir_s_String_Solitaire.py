t = int(input())

for _ in range(t):
    s = input().strip()
    a = s.count('A')
    b = s.count('B')
    c = s.count('C')

    if b == a + c:
        print("YES")
    else:
        print("NO")
