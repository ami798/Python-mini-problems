import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, m, k = map(int, sys.stdin.readline().split())
        if n == 1:
            print(min(m, k))
        elif m == 1:
            print(1 if k <= n else k - n + 1)
        else:
            max_per_row = (k + n - 1) // n  # Equivalent to ceil(k / n)
            if max_per_row <= m:
                print(max_per_row)
            else:
                # All rows have m desks, but need to distribute the remaining
                # Here, the max bench length is m
                print(m)

solve()