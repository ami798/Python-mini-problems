t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().strip().split()))

    # Frequency dictionary
    freq = {}
    for num in a:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    # Find the maximum frequency
    max_freq = max(freq.values())

    # Calculate the minimum cost
    cost = n - max_freq

    # Print the result
    print(cost)
