import sys
import math

def precompute_prime_factors(max_num):
    spf = [0] * (max_num + 1)
    spf[0] = spf[1] = 1
    for i in range(2, max_num + 1):
        if spf[i] == 0:
            spf[i] = i
            for j in range(i * i, max_num + 1, i):
                if spf[j] == 0:
                    spf[j] = i
    return spf

def factorize(x, spf):
    factors = {}
    while x > 1:
        p = spf[x]
        while x % p == 0:
            factors[p] = factors.get(p, 0) + 1
            x = x // p
    return factors

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    spf = precompute_prime_factors(10**5)
    results = []
    for _ in range(t):
        n, q = map(int, input[ptr:ptr + 2])
        ptr += 2
        a = list(map(int, input[ptr:ptr + n]))
        ptr += n
        # Precompute prime factors for each a[i]
        a_factors = []
        for num in a:
            a_factors.append(factorize(num, spf))
        for __ in range(q):
            k, l, r = map(int, input[ptr:ptr + 3])
            ptr += 3
            current_k = k
            total = 0
            for i in range(l - 1, r):
                temp_k = current_k
                factors_k = factorize(temp_k, spf)
                factors_ai = a_factors[i]
                # Divide temp_k by a[i] as much as possible
                for p in factors_ai:
                    if p in factors_k:
                        exponent = min(factors_k[p], factors_ai[p])
                        temp_k = temp_k // (p ** exponent)
                total += temp_k
            results.append(str(total))
    print('\n'.join(results))

solve()