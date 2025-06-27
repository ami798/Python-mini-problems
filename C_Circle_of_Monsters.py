import sys
input = sys.stdin.read

def solve():
    data = input().split()
    index = 0
    T = int(data[index])
    index += 1
    res = []
    
    for _ in range(T):
        n = int(data[index])
        index += 1
        a = []
        b = []
        for _ in range(n):
            ai = int(data[index])
            bi = int(data[index + 1])
            a.append(ai)
            b.append(bi)
            index += 2

        total = 0
        min_extra = float('inf')

        for i in range(n):
            prev = (i - 1 + n) % n
            need = max(0, a[i] - b[prev])
            total += need
            min_extra = min(min_extra, a[i] - need)

        res.append(str(total + min_extra))

    print("\n".join(res))

solve()
