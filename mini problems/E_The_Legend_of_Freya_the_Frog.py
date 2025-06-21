import math
t=int(input())
for _ in range(t):
    x,y,k=map(int,input().split())
    x_ways=math.ceil(x/k)
    y_ways=math.ceil(y/k)
    if x_ways>y_ways:
        total=2*x_ways-1
    else:
        total=2*y_ways
    print(total)