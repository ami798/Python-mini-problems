s=input().strip()
n=len(s)
q=[0]*n
for i in range(1,n):
    q[i]=q[i-1]+(1 if s[i] == s[i-1] else 0)
f=int(input())
for _ in range(f):
    l,r=map(int,input().split())
    print(q[r-1]-q[l-1])
