import sys

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n, k, x = map(int, input[ptr:ptr+3])
        ptr +=3
        a = list(map(int, input[ptr:ptr+n]))
        ptr +=n
        
        prefix = [0]*(n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + a[i]
        S = prefix[n]
        
        res = 0
        if S <=0:
            
            max_suffix = [0]*(n+2)
            max_suffix[n] = 0
            for i in range(n-1, -1, -1):
                max_suffix[i] = max(a[i], a[i] + max_suffix[i+1])
            for l in range(n):
                if max_suffix[l] >=x:
                    res +=k
                else:
                    pass
        else:
            # For each l in 0..n-1, find the minimal m such that (prefix[n] - prefix[l]) + m*S >=x
            # Then, the number of starting positions is (k - m)
            # Also, need to handle cases where m can be negative (i.e., no need for full copies)
            for l in range(n):
                remaining_sum = prefix[n] - prefix[l]
                if remaining_sum >=x:
                    res +=k
                    continue
                required = x - remaining_sum
                m = (required + S -1) // S  # Ceiling division
                if m <0:
                    m=0
                if m <k:
                    res += (k - m)
        print(res)

solve()