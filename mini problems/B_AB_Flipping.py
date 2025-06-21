t=int(input())
for _ in range(t):
    n=int(input())
    s=list(input())
    count=0
    used=[False] * (n-1)
    changed=True
    while changed:
        changed=False
        for i in range(n-1):
            if not used[i] and s[i]=='A' and s[i+1]=='B':
                s[i],s[i+1]=s[i+1],s[i]
                used[i]=True
                count+=1
                changed=True
    print(count)