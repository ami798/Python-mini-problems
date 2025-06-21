t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    total=sum(a)
    prefix_sum=0
    happy=True
    for i in range(n-1):
        prefix_sum+=a[i]
        if prefix_sum >=total:
            happy=False
            break
    if happy:
        suff_sum=0
        for i in range(n-1 ,0, -1):
            suff_sum+=a[i]
            if suff_sum>=total:
                happy=False
                break
    print("YES" if happy else "NO")
