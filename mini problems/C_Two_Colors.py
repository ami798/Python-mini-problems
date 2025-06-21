import sys

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n, m = map(int, input[ptr:ptr+2])
        ptr +=2
        a = list(map(int, input[ptr:ptr+m]))
        ptr +=m
        
        a.sort()
        total = 0
        prefix = [0]*(m+1)
        for i in range(m):
            prefix[i+1] = prefix[i] + a[i]
        
        res = 0
        for i in range(m):
            if a[i] > n:
                continue
            max_other = n - a[i]
            # Find the largest a[j] <= max_other
            left, right = 0, m
            while left < right:
                mid = (left + right) //2
                if a[mid] > max_other:
                    right = mid
                else:
                    left = mid +1
            cnt = left
            if cnt > i:
                cnt -=1
            res += cnt *2
        
        print(res)

solve()