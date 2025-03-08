def mtcp(n, positions):
    max_time = 0
    
    for pos in positions:
        me = abs(pos - 1)
        fre = abs(pos - 106)
        max_time = max(max_time, min(me, fre))
    
    return max_time


n = int(input())
positions = list(map(int, input().split()))


result = mtcp(n, positions)
print(result)
