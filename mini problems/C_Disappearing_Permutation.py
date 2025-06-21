import sys

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n = int(input[ptr])
        ptr += 1
        p = list(map(int, input[ptr:ptr + n]))
        ptr += n
        d = list(map(int, input[ptr:ptr + n]))
        ptr += n
        
        # Create a list to map original positions to their values
        original = p.copy()
        # We need to track which positions have been zeroed
        zeroed = [False] * (n + 1)  # 1-based indexing
        operations = 0
        res = []
        
        for i in range(n):
            pos = d[i]
            # Check if the original value was not equal to its index
            if original[pos - 1] != pos:
                operations += 1
            zeroed[pos] = True
            res.append(str(operations))
        
        print(' '.join(res) + ' ')

solve()