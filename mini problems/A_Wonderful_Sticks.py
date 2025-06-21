t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    res = []
    left = 0
    while left < n - 1:
        right = left
        if s[right] == '<':
            while right < n - 1 and s[right] == '<':
                right += 1
            # The segment from left to right is <...<
            # The corresponding numbers should be increasing then place the smallest remaining at the end
            # Alternatively, think of it as the next elements are smaller than all before
            # So, the initial approach might need adjustment
            pass
        else:
            while right < n - 1 and s[right] == '>':
                right += 1
            # The segment from left to right is >...>
            # The corresponding numbers should be decreasing then place the largest remaining at the end
            pass
        # More precise approach: process the string in a way that for each < or >, we pick the next number appropriately
        left = right
    # Alternative approach inspired by recognizing that the solution can be constructed by reversing segments
    # Another idea: the answer can be constructed by assigning the largest numbers to the left for < segments and smallest for > segments
    # Let's think of the string as a series of directions, and we can process them by tracking the ranges
    
    # Initialize the answer array
    ans = []
    low = 1
    high = n
    # We process the string to determine the numbers
    for i in range(n - 1):
        if s[i] == '<':
            ans.append(low)
            low += 1
        else:
            ans.append(high)
            high -= 1
    ans.append(low)  # or high, since low == high at this point
    print(' '.join(map(str, ans)))