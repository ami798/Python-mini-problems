import sys
import math

MOD = 998244353

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n, m, d = map(int, input[ptr:ptr+3])
        ptr +=3
        grid = []
        for _ in range(n):
            grid.append(input[ptr])
            ptr +=1
        
        # Collect holds for each level (1-based to n-based)
        levels = [[] for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'X':
                    levels[i+1].append((i+1, j+1))  # (row, column)
        
        # Check if all levels have at least one hold
        possible = True
        for i in range(1, n+1):
            if not levels[i]:
                possible = False
                break
        if not possible:
            print(0)
            continue
        
        # Initialize DP: dp[i][j] = number of ways to reach hold j on level i
        # We'll process levels from bottom (n) to top (1)
        # Initialize for level n
        dp_prev = {}
        for idx, (r, c) in enumerate(levels[n]):
            dp_prev[idx] = 1
        
        for i in range(n-1, 0, -1):
            current_holds = levels[i]
            prev_holds = levels[i+1]
            dp_current = {}
            for idx_curr, (r_curr, c_curr) in enumerate(current_holds):
                total = 0
                for idx_prev, (r_prev, c_prev) in enumerate(prev_holds):
                    dx = r_curr - r_prev
                    dy = c_curr - c_prev
                    distance_sq = dx*dx + dy*dy
                    if distance_sq <= d*d:
                        total += dp_prev.get(idx_prev, 0)
                        total %= MOD
                dp_current[idx_curr] = total
            dp_prev = dp_current
        
        # Sum all ways to reach any hold on level 1
        result = 0
        for cnt in dp_prev.values():
            result += cnt
            result %= MOD
        print(result)

solve()




