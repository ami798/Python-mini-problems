
n = int(input())  
times = list(map(int, input().split()))  


left = 0 
right = n - 1  
time_mieraf = 0 
time_naol = 0  
bars_mieraf = 0  
bars_naol = 0  


while left <= right:
    if time_mieraf <= time_naol:
        time_mieraf += times[left]
        bars_mieraf += 1
        left += 1
    else:
        time_naol += times[right]
        bars_naol += 1
        right -= 1


print(bars_mieraf, bars_naol)
