t = int(input().strip())
results = []

for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().strip().split()))

    # Initialize the output array and a frequency array
    b = [0] * n
    freq = [0] * (n + 1)
    
    # Fill the array b
    for i in range(n):
        if freq[a[i]] < a[i]:
            b[i] = a[i]
        else:
            # Find the smallest unused number in the range [1, n]
            for j in range(1, n + 1):
                if freq[j] < j:
                    b[i] = j
                    break
        freq[b[i]] += 1
    
    results.append(" ".join(map(str, b)))

print("\n".join(results))
