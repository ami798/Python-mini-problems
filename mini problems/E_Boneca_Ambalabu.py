import sys

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    results = []
    for _ in range(t):
        n = int(input[ptr])
        ptr += 1
        a = list(map(int, input[ptr:ptr + n]))
        ptr += n
        
        # Precompute the count of set bits for each bit position (0 to 29)
        bit_counts = [0] * 30
        for num in a:
            for b in range(30):
                if num & (1 << b):
                    bit_counts[b] += 1
        
        max_sum = 0
        for num in a:
            current_sum = 0
            for b in range(30):
                if num & (1 << b):
                    current_sum += (n - bit_counts[b]) * (1 << b)
                else:
                    current_sum += bit_counts[b] * (1 << b)
            if current_sum > max_sum:
                max_sum = current_sum
        results.append(max_sum)
    
    print('\n'.join(map(str, results)))

solve()