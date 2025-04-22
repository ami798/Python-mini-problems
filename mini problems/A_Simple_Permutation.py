def simple_permutation():
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])  # Number of test cases
    results = []

    for i in range(t):
        n = int(data[i + 1])  # Size of the permutation
        # We can construct the permutation as follows:
        permutation = list(range(2, n + 1)) + [1]
        results.append(" ".join(map(str, permutation)))

    # Output all results
    sys.stdout.write("\n".join(results) + "\n")

