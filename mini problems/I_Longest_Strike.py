import sys
from collections import defaultdict

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n, k = map(int, input[ptr:ptr+2])
        ptr += 2
        a = list(map(int, input[ptr:ptr+n]))
        ptr += n
        
        freq = defaultdict(int)
        for num in a:
            freq[num] += 1
        
        valid_numbers = []
        for num in freq:
            if freq[num] >= k:
                valid_numbers.append(num)
        
        if not valid_numbers:
            print(-1)
            continue
        
        valid_numbers.sort()
        max_length = 1
        current_length = 1
        best_l = valid_numbers[0]
        best_r = valid_numbers[0]
        current_l = valid_numbers[0]
        
        for i in range(1, len(valid_numbers)):
            if valid_numbers[i] == valid_numbers[i-1] + 1:
                current_length += 1
                if current_length > max_length:
                    max_length = current_length
                    best_l = current_l
                    best_r = valid_numbers[i]
            else:
                current_length = 1
                current_l = valid_numbers[i]
        
        if max_length == 1:
            # All valid numbers are isolated, pick any
            print(valid_numbers[0], valid_numbers[0])
        else:
            print(best_l, best_r)

solve()