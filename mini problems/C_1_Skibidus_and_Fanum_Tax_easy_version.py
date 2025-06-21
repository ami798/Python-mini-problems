def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])  # Number of test cases
    index = 1
    results = []

    for _ in range(t):
        # Read n and m (though m = 1 here)
        n, m = int(data[index]), int(data[index + 1])
        index += 2

        # Read array a and b
        a = list(map(int, data[index:index + n]))
        b = int(data[index + n])  # Only one element in b
        index += (n + m)

        # Check if we can make the array non-decreasing
        # Original and transformed values
        original = sorted(a)  # Original array sorted
        transformed = sorted([b - x for x in a])  # Transformed values sorted
        
        # Verify if either original or transformed can be rearranged
        can_sort = True
        for i in range(n):
            if original[i] > transformed[i]:
                can_sort = False
                break

        # Append YES or NO based on feasibility
        results.append("YES" if can_sort else "NO")

    # Output results
    sys.stdout.write("\n".join(results) + "\n")

