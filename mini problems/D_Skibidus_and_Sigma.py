def solve():
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])  # Number of test cases
    index = 1
    results = []

    for _ in range(t):
        # Read n and m
        n, m = map(int, data[index:index + 2])
        index += 2

        # Read all arrays
        arrays = []
        for i in range(n):
            arrays.append(list(map(int, data[index:index + m])))
            index += m

        # Sort arrays by their total sum in descending order
        arrays.sort(key=lambda x: sum(x), reverse=True)

        # Calculate the maximum score
        prefix_sum = 0
        total_score = 0
        for arr in arrays:
            prefix_sum += sum(arr)
            total_score += prefix_sum

        # Store the result for this test case
        results.append(total_score)

    # Output all results
    for res in results:
        print(res)
