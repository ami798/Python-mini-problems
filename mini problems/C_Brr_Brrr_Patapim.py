import sys

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n = int(input[ptr])
        ptr += 1
        grid = []
        for _ in range(n):
            row = list(map(int, input[ptr:ptr + n]))
            ptr += n
            grid.append(row)
        
        # The permutation is of size 2n
        size = 2 * n
        permutation = [0] * (size + 1)  # 1-based indexing
        
        # We need to find p_1 to p_{2n}
        # p_1 is not present in the grid (since i + j >= 2)
        # So, p_1 is the missing number in the grid's possible values (1..2n)
        present = set()
        for i in range(n):
            for j in range(n):
                present.add(grid[i][j])
        for num in range(1, size + 1):
            if num not in present:
                permutation[1] = num
                break
        
        # Now, for each k from 2 to 2n, p_k is the value in the grid where i + j = k
        # For each k, collect all grid[i][j] where i + j = k
        # The value p_k must be one of these, and it should not have been used before
        used = set()
        used.add(permutation[1])
        for k in range(2, size + 1):
            candidates = set()
           
            start_i = max(1, k - n)
            end_i = min(n, k - 1)
            for i in range(start_i, end_i + 1):
                j = k - i
                if 1 <= j <= n:
                    candidates.add(grid[i - 1][j - 1])
            # p_k is the candidate not used yet
            for num in candidates:
                if num not in used:
                    permutation[k] = num
                    used.add(num)
                    break
        
        print(' '.join(map(str, permutation[1:size + 1])) + ' ')

solve()