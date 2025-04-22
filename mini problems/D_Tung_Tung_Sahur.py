def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        p = data[idx]
        idx += 1
        s = data[idx]
        idx += 1
        
        len_p = len(p)
        len_s = len(s)
        
        # Check if the length of s is within the possible range
        if len_s < len_p or len_s > 2 * len_p:
            results.append("NO")
            continue
        
        i = 0  # pointer for p
        j = 0  # pointer for s
        possible = True
        
        while i < len_p and j < len_s:
            current_p = p[i]
            current_s = s[j]
            
            if current_s != current_p:
                possible = False
                break
            
            # Check if the next character is the same (double hit)
            if j + 1 < len_s and s[j + 1] == current_p:
                j += 2
            else:
                j += 1
            i += 1
        
        # After processing all characters in p, check if we've processed all characters in s
        if possible and j == len_s and i == len_p:
            results.append("YES")
        else:
            results.append("NO")
    
    print('\n'.join(results))

solve()