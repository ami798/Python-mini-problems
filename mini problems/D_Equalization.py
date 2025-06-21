import sys

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        x, y = map(int, input[ptr:ptr+2])
        ptr += 2
        if x == y:
            print(0)
            continue
        if x == 0 or y == 0:
            non_zero = x if x != 0 else y
            k = 0
            while (1 << k) <= non_zero:
                k += 1
            print(1 << (k - 1))
            continue
        used_k = set()
        cost = 0
        while x != y:
            if x > y:
                diff = x - y
                k = 0
                while (1 << (k + 1)) <= diff:
                    k += 1
                while k in used_k:
                    k -= 1
                    if k < 0:
                        break
                if k < 0:
                    k = 0
                    while k in used_k:
                        k += 1
                used_k.add(k)
                x = x // (1 << k)
                cost += (1 << k)
            else:
                diff = y - x
                k = 0
                while (1 << (k + 1)) <= diff:
                    k += 1
                while k in used_k:
                    k -= 1
                    if k < 0:
                        break
                if k < 0:
                    k = 0
                    while k in used_k:
                        k += 1
                used_k.add(k)
                y = y // (1 << k)
                cost += (1 << k)
        print(cost)

solve()