import sys

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n, q = map(int, input[ptr:ptr+2])
        ptr += 2
        a = list(map(int, input[ptr:ptr+n]))
        ptr += n
        
        total_sum = sum(a)
        prefix_odd = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_odd[i] = prefix_odd[i-1] + (a[i-1] % 2)
        
        output = []
        for __ in range(q):
            l, r, k = map(int, input[ptr:ptr+3])
            ptr += 3
            range_len = r - l + 1
            original_odd = prefix_odd[r] - prefix_odd[l-1]
            new_odd = (k % 2) * range_len
            total_parity = total_sum % 2
            new_total_parity = (total_parity - original_odd + new_odd) % 2
            output.append("YES" if new_total_parity == 1 else "NO")
        
        print('\n'.join(output))

solve()