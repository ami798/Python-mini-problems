def solve():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n, k = map(int, input[ptr:ptr + 2])
        ptr += 2
        s = input[ptr]
        ptr += 1
        
        reversed_s = s[::-1]
        if s < reversed_s:
            print("YES")
            continue
        
        # We need to make s < reversed_s with at most k swaps
        # The minimal swaps is the number of positions where s[i] > reversed_s[i]
        # But we can also consider that swapping can make s lex smaller than reversed_s
        # So we need to find the minimal swaps to make s < reversed_s
        # One approach is to find the first position where s differs from reversed_s and make s[i] < reversed_s[i]
        
        # Another approach is to count the number of positions where s[i] != reversed_s[i]
        # Each swap can fix at most two such positions (if we swap s[i] and s[j] where i and j are symmetric)
        
        # Let's find the minimal number of swaps needed to make s < reversed_s
        # The minimal swaps is the minimal number of changes needed to make s < reversed_s
        # This can be done by comparing s and reversed_s and counting the necessary changes
        
        # We can iterate through the string and count the number of positions where s[i] > reversed_s[i]
        # Each such position requires at least one swap to make s[i] < reversed_s[i]
        
        # However, swapping s[i] and s[j] can affect both positions i and j
        
        # So the minimal swaps is the ceiling of (number of positions where s[i] > reversed_s[i]) / 2
        
        count = 0
        for i in range(n):
            if s[i] > reversed_s[i]:
                count += 1
        
        minimal_swaps = (count + 1) // 2
        
        if minimal_swaps <= k:
            print("YES")
        else:
            print("NO")

solve()