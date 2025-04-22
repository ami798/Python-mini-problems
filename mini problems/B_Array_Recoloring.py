import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        a_sorted = sorted(a, reverse=True)
        initial_sum = sum(a_sorted[:k])
        last_element = a_sorted[k] if k < n else 0
        total_cost = initial_sum + last_element
        print(total_cost)

solve()