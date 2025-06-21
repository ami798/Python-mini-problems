n=int(input())
times=list(map(int,input().split()))
times.sort()
wt=0
count=0
for t in times:
    if wt<=t:
        count+=1
        wt+=t
print(count)