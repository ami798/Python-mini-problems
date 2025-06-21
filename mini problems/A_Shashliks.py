t = int(input())
for _ in range(t):
    k, a, b, x, y = map(int, input().split())

    
    temp = k
    cnt1 = 0
    while temp >= a:
        cnt1 += 1
        temp -= x
    temp2 = temp
    cnt2 = 0
    while temp2 >= b:
        cnt2 += 1
        temp2 -= y
    total1 = cnt1 + cnt2

    
    temp = k
    cnt1 = 0
    while temp >= b:
        cnt1 += 1
        temp -= y
    temp2 = temp
    cnt2 = 0
    while temp2 >= a:
        cnt2 += 1
        temp2 -= x
    total2 = cnt1 + cnt2

    print(max(total1, total2))
