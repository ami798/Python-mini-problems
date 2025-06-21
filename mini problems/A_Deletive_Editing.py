def solve():
    n = int(input())
    for _ in range(n):
        s, t = input().split()
        if len(t) > len(s):
            print("NO")
            continue
        
        # Check character frequencies
        from collections import defaultdict
        freq_s = defaultdict(int)
        freq_t = defaultdict(int)
        for char in s:
            freq_s[char] += 1
        for char in t:
            freq_t[char] += 1
        
        possible = True
        for char in freq_t:
            if freq_t[char] > freq_s[char]:
                possible = False
                break
        if not possible:
            print("NO")
            continue
        
        # Check if t is a possible result
        i = 0
        j = 0
        len_s = len(s)
        len_t = len(t)
        while i < len_s and j < len_t:
            if s[i] == t[j]:
                j += 1
            i += 1
        
        if j == len_t:
            print("YES")
        else:
            print("NO")

solve()