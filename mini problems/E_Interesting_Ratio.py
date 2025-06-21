import sys

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    test_cases = list(map(int, input[ptr:ptr + t]))
    ptr += t

    max_n = max(test_cases)
    
    # Sieve of Eratosthenes to find all primes up to max_n
    sieve = bytearray([1]) * (max_n + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, int(max_n ** 0.5) + 1):
        if sieve[i]:
            sieve[i*i : max_n + 1 : i] = b'\x00' * len(sieve[i*i : max_n + 1 : i])
    
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    
    # Precompute the number of primes up to each n
    prime_count = [0] * (max_n + 1)
    count = 0
    for i in range(2, max_n + 1):
        if sieve[i]:
            count += 1
        prime_count[i] = count
    
    # Function to compute the answer for a given n
    def compute_answer(n):
        res = 0
        for p in primes:
            if p > n:
                break
            res += n // p
        return res
    
    # Process each test case
    output = []
    for n in test_cases:
        output.append(str(compute_answer(n)))
    
    print('\n'.join(output))

solve()