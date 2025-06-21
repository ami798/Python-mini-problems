t=int(input())
for _ in range(t):
    n,k,q=map(int,input().split())
    a=list(map(int,input().split()))
    count=0
    length=0
    for i in a+[q+1]:
        if i<=q:
            length+=1
        else:
            if length>=k:
                valid=length-k+1
                count+=valid*(valid+1)//2
            length=0

    print(count)