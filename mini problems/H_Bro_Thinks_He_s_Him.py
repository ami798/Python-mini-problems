MOD = 998244353

def solve():
    # Read number of test cases
    t = int(input())
    for _ in range(t):
        # Read the binary string
        s = list(input().strip())
        n = len(s)
        
        # Read number of queries and query positions
        q = int(input())
        queries = list(map(int, input().split()))
        
        # Initialize result list for this test case
        results = []
        
        # Compute initial f(t) for the string
        f_t = 0
        for i in range(1, n):
            if s[i] != s[i-1]:
                f_t += 1
        f_t += 1  # Count the last partition

        # Process each query
        for v in queries:
            # Convert 1-based index to 0-based
            v -= 1
            
            # Flip the character
            s[v] = '1' if s[v] == '0' else '0'
            
            # Update f(t) based on changes in partitions
            if v > 0 and s[v] != s[v-1]:
                f_t += 1
            elif v > 0 and s[v] == s[v-1]:
                f_t -= 1
            
            if v < n-1 and s[v] != s[v+1]:
                f_t += 1
            elif v < n-1 and s[v] == s[v+1]:
                f_t -= 1
            
            # Save result modulo MOD
            results.append(f_t % MOD)
        
        # Output results for this test case
        print(" ".join(map(str, results)))

# Main execution
solve()
