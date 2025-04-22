def solve():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n = int(input[ptr])
        ptr += 1
        s = input[ptr]
        ptr += 1
        
        sorted_s = ''.join(sorted(s))
        if s == sorted_s:
            print(0)
            continue
        
        k = 0
        for original_char, sorted_char in zip(s, sorted_s):
            if original_char != sorted_char:
                k += 1
        print(k)

solve()