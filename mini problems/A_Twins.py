n=int(input())
coins=list(map(int,input().split()))
total=sum(coins)
coins.sort(reverse=True)
my_sum=0
count=0
for coin in coins:
    my_sum+=coin
    total-=coin
    count+=1
    if my_sum>total:
        break
print(count)


