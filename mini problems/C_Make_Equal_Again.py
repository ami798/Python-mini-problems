def solve():
    t = int(input().strip())  # Number of test cases

    for _ in range(t):
        n = int(input().strip())  # Size of array
        a = list(map(int, input().split()))  # Array elements

        # Find the most frequent element
        freq = {}
        for num in a:
            freq[num] = freq.get(num, 0) + 1
        
        max_freq = max(freq.values())  # Highest occurrence of any element
        best_element = max(freq, key=freq.get)  # Most frequent element

        # Calculate minimum cost
        cost, i = 0, 0
        while i < n:
            if a[i] != best_element:
                j = i
                while j < n and a[j] != best_element:
                    j += 1  # Find the largest block needing change
                cost = max(cost, j - i)  # Update cost
                i = j
            else:
                i += 1

        print(cost)  # Output result for this test case

# Call the function to run the program
solve()