def solve():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        min_so_far = float('inf')
        bad_days = 0
        for num in reversed(a):
            if num > min_so_far:
                bad_days += 1
            else:
                min_so_far = num
        results.append(bad_days)
    print('\n'.join(map(str, results)))

solve()