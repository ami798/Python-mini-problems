
n, t, c = map(int, input().split())
crime_severities = list(map(int, input().split()))

valid_count = 0
current_window_count = 0


for i in range(n):
    if crime_severities[i] <= t:
        current_window_count += 1  
    else:
        current_window_count = 0 

    
    if current_window_count >= c:
        valid_count += 1


print(valid_count)
