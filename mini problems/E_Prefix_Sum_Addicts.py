t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    s=list(map(int,input().split()))
    if k==1:
        print("Yes")
        continue
    a=[s[i] -s[i-1] for i in range(1,k)]
    if any (a[i]<a[i-1] for i in range (1,k-1)):
        print("No")
        continue
    if s[0]>a[0] * (n-k+1):
        print("No")
        continue
    print("Yes")
    

