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
        arr = list(map(int, input[ptr:ptr + n]))
        ptr += n
        
        
        count_1 = 0
        initial_inversions = 0
        for num in arr:
            if num == 1:
                count_1 += 1
            else:
                initial_inversions += count_1
        
        max_inversions = initial_inversions
        
        
        count_0_right = [0] * n
        count_0 = 0
        for i in range(n - 1, -1, -1):
            if arr[i] == 0:
                count_0 += 1
            count_0_right[i] = count_0
        
        
        count_1_left = [0] * n
        count_1_l = 0
        for i in range(n):
            if arr[i] == 1:
                count_1_l += 1
            count_1_left[i] = count_1_l
        
        
        for i in range(n):
            if arr[i] == 0:
                
                
                delta = (count_0_right[i] - 1) - count_1_left[i]
                max_inversions = max(max_inversions, initial_inversions + delta)
        
        # Try flipping each 1 to 0
        for i in range(n):
            if arr[i] == 1:

                delta = (count_1_left[i] - 1) - count_0_right[i]
                max_inversions = max(max_inversions, initial_inversions + delta)
        
        results.append(max_inversions)
    
    print('\n'.join(map(str, results)))

solve()