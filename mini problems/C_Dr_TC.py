t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    ones = s.count('1')
    zeros = n - ones
    total_ones = (n - 1) * ones + zeros
    print(total_ones)
