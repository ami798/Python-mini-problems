import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        s = sys.stdin.readline().strip()
        n = len(s)
        if n == 0:
            print(0)
            continue
        total_ones = s.count('1')
        if total_ones == 0:
            print(0)
            continue
        if total_ones == n:
            print(n * n)
            continue
        
        max_run = 0
        current = 0
     
        doubled = s + s
        current_run = 0
        max_run_non_circular = 0
        for c in doubled:
            if c == '1':
                current_run += 1
                max_run_non_circular = max(max_run_non_circular, current_run)
            else:
                current_run = 0
        max_run = min(max_run_non_circular, n)
        
        res = 0
        h = (max_run + 1) // 2
        w = (max_run + 2) // 2
        res = h * w
        print(res)

solve()