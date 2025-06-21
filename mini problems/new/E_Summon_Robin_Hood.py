import sys
import bisect

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n = int(input[ptr])
        ptr += 1
        a = list(map(int, input[ptr:ptr + n]))
        ptr += n
        
        a_sorted = sorted(a)
        total = sum(a)
        max_a = a_sorted[-1]
        
        # Check if already more than half are unhappy without adding any x
        new_total = total
        half_avg = new_total / (2 * n)
        cnt = bisect.bisect_left(a_sorted, half_avg)
        if cnt > n // 2:
            print(0)
            continue
        
        # Binary search for the minimal x
        left = 0
        right = 10**18
        answer = -1
        while left <= right:
            mid = (left + right) // 2
            new_total = total + mid
            half_avg = new_total / (2 * n)
            cnt = bisect.bisect_left(a_sorted, half_avg)
            if cnt > n // 2:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        print(answer)

solve()