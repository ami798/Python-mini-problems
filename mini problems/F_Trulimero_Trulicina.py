import sys

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    results = []
    for _ in range(t):
        n = int(input[ptr])
        m = int(input[ptr + 1])
        k = int(input[ptr + 2])
        ptr += 3
        
        grid = [[0 for _ in range(m)] for _ in range(n)]
        current = 1
        
        for i in range(n):
            for j in range(m):
                grid[i][j] = current
                current += 1
                if current > k:
                    current = 1
        
        # Ensure no two adjacent cells have the same value
        # We can adjust by shifting the starting point in each row
        for i in range(n):
            if i % 2 == 1 and m > 1:
                # Shift the row to avoid adjacent duplicates
                first = grid[i][0]
                for j in range(m - 1):
                    grid[i][j] = grid[i][j + 1]
                grid[i][m - 1] = first
        
        # Verify the counts
        count = [0] * (k + 1)
        for i in range(n):
            for j in range(m):
                count[grid[i][j]] += 1
        
        # Verify no adjacent duplicates
        valid = True
        for i in range(n):
            for j in range(m):
                if i > 0 and grid[i][j] == grid[i - 1][j]:
                    valid = False
                if j > 0 and grid[i][j] == grid[i][j - 1]:
                    valid = False
                if not valid:
                    break
            if not valid:
                break
        
        if not valid:
            # If not valid, use a different pattern
            current = 1
            for i in range(n):
                for j in range(m):
                    grid[i][j] = current
                    current = current % k + 1
        
        # Prepare the output
        grid_str = []
        for row in grid:
            grid_str.append(' '.join(map(str, row)))
        results.append('\n'.join(grid_str))
    
    print('\n'.join(results))

solve()