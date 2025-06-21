t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    max_product=0
    for i in range (n):
        temp=a[i]
        a[i]+=1
        product=1
        for num in a:
           product*=num
        max_product=max(max_product,product)
        a[i]=temp
    print(max_product)
