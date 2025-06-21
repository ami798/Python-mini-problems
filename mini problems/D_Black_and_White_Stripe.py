t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    s=input()
    curr_w=s[:k].count('W')
    min_w=curr_w
for i in range(k,n):
    if s[i-k]=='W':
        curr_w-=1
    if s[i]=='W':
        curr_w+=1
    min_w=min(min_w,curr_w)
print(min_w)
