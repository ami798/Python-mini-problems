t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()
    
    char= {}
    
    possible = True
    
    for i in range(len(s)):
        if s[i] not in char:
            if i > 0 and char.get(s[i - 1], -1) == 0:
                char[s[i]] = 1
            else:
                char[s[i]] = 0
        else:
            if char[s[i]] == char.get(s[i - 1], -1):
                possible = False
                break
    
    if possible:
        print("YES")
    else:
        print("NO")
