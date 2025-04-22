import sys
MOD = 998244353

def main():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    
    max_n = 5 * 10**5 + 10
    fact = [1] * (max_n)
    inv_fact = [1] * (max_n)
    
    for i in range(1, max_n):
        fact[i] = fact[i-1] * i % MOD
    
    inv_fact[max_n-1] = pow(fact[max_n-1], MOD-2, MOD)
    for i in range(max_n-2, -1, -1):
        inv_fact[i] = inv_fact[i+1] * (i+1) % MOD
    
    for _ in range(t):
        c = list(map(int, input[ptr:ptr+26]))
        ptr += 26
        
        total = sum(c)
        if total == 0:
            print(0)
            continue
        
        # Precompute possible even and odd counts
        max_even = (total + 1) // 2
        max_odd = total // 2
        
        # Initialize DP: dp[e][o] = number of ways to have e even and o odd
        # Since e + o = sum(c), we can use a 1D DP
        # We'll use a dictionary or a list to represent current state
        dp = {}
        dp[(0, 0)] = 1
        
        for ci in c:
            if ci == 0:
                continue
            new_dp = {}
            for (e, o), ways in dp.items():
                # Assign all ci to even
                new_e = e + ci
                new_o = o
                if new_e <= max_even:
                    key = (new_e, new_o)
                    new_dp[key] = (new_dp.get(key, 0) + ways) % MOD
                # Assign all ci to odd
                new_e = e
                new_o = o + ci
                if new_o <= max_odd:
                    key = (new_e, new_o)
                    new_dp[key] = (new_dp.get(key, 0) + ways) % MOD
            dp = new_dp
        
        res = 0
        for (e, o), ways in dp.items():
            if e + o != total:
                continue
            # Compute multinomial coefficients
            # Ways to arrange even positions: fact[e] / product(fact[ci] for ci in even)
            # Similarly for odd
            # Since we don't track which letters are even/odd, we need another approach
            # Instead, realize that the multinomial coefficient is fact[total] / (product fact[ci])
            # But since all ci are assigned to either even or odd, the arrangement is fact[e] * fact[o] / product(fact[ci])
            # But we need to know which ci are assigned to even and odd, which isn't tracked in DP
            # So this approach needs adjustment
            # Alternative idea: The total number of ways is (ways to partition) * (multinomial coefficient)
            # But the multinomial coefficient is the same for all partitions, since it's fact[total] / product(fact[ci])
            # So the answer is sum_{valid partitions} (ways to partition) * (multinomial coefficient)
            # But the multinomial coefficient is the same, so it's (sum ways) * (multinomial coefficient)
            # So we can compute the multinomial coefficient separately
            pass
        
        # Compute multinomial coefficient: fact[total] / product(fact[ci] for ci in c)
        denominator = 1
        for ci in c:
            denominator = denominator * inv_fact[ci] % MOD
        multinomial = fact[total] * denominator % MOD
        
        # The total number of valid strings is sum_{valid partitions} (ways to partition) * multinomial
        # But since all partitions are valid (they satisfy e <= max_even and o <= max_odd), and e + o = total
        # So the answer is (sum of ways) * multinomial
        sum_ways = 0
        for (e, o), ways in dp.items():
            if e + o == total:
                sum_ways = (sum_ways + ways) % MOD
        res = sum_ways * multinomial % MOD
        print(res)

if __name__ == '__main__':
    main()