import sys

def min_operations(n, k):
    operations = 0
    while n > 0:
        if n % 2 == 0:
            
            x = min(n, k - 1)
            if x == 0:
                x = 2  
            q = n // x
            operations += q
            n -= q * x
        else:
            
            x = min(n, k)
            operations += 1
            n -= x
    return operations

t = int(sys.stdin.readline())
for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    print(min_operations(n, k))