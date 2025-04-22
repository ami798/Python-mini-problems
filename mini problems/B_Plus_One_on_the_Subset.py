t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    min_val = min(array)
    max_val = max(array)
    print(max_val - min_val)