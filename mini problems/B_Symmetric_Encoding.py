t = int(input())
for _ in range(t):
    
    b = input()
    r = sorted(set(b))
    new = {}
    for i in range(len(r)):
        new[r[i]] = r[len(r) - 1 - i]

    
    s = ''.join(new[ch] for ch in b)
    print(s)
