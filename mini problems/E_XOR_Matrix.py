MOD = 998244353

def count_valid_pairs(n, m, A, B):
    # Function to count valid pairs
    total_count = 0

    for x1 in range(A + 1):
        for x2 in range(x1, A + 1):
            if is_valid(x1, x2, n, m, A, B):
                total_count += compute_pairs(x1, x2, n, m, A, B)
                total_count %= MOD
    return total_count

def is_valid(x1, x2, n, m, A, B):
    # Verify if arrays can generate the XOR matrix
    distinct_values = set()
    for a in range(A + 1):
        for b in range(B + 1):
            distinct_values.add(a ^ b)
    return len(distinct_values) <= 2

def compute_pairs(x1, x2, n, m, A, B):
    # Compute valid combinations of arrays a and b
    ways_a = pow(A + 1, n, MOD)  # Ways to form array 'a'
    ways_b = pow(B + 1, m, MOD)  # Ways to form array 'b'
    return (ways_a * ways_b) % MOD

# Reading input
t = int(input())
results = []
for _ in range(t):
    n, m, A, B = map(int, input().split())
    result = count_valid_pairs(n, m, A, B)
    results.append(result)

# Print results for each test case
for res in results:
    print(res)