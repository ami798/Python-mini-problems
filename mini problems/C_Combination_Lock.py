import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        if n % 2 == 0:
            print(-1)
        else:
            permutation = []
            for i in range(1, n + 1):
                val = (2 * i - 1) % n
                if val == 0:
                    val = n
                permutation.append(str(val))
            print(' '.join(permutation))

solve()