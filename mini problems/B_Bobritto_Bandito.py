t = int(input())
for _ in range(t):
    n, m, l, r = map(int, input().split())
    # The segment on day m must have length m (since day 0 has length 1, day 1 has length 2, ..., day m has length m+1)
    # But the problem expects the output to have length m (e.g., day 2 has length 2 in the first test case)
    # So we need to adjust our approach to match the expected output
    # From the sample input, it seems the segment on day m has length m, not m+1
    # So the segment [l', r'] should satisfy r' - l' + 1 = m
    # Or perhaps the problem considers day 0 as length 1, day 1 as length 2, etc., but the sample expects r' - l' = m - 1
    # To match the sample, we need to output segments where r' - l' = m - 1
    # For the first test case: n=4, m=2, l=-2, r=2
    # Expected output: -1 1, which has length 3 (1 - (-1) = 2, but 1 - (-1) + 1 = 3)
    # Wait, the note says day 2 has segment [-1,1], which has length 3 (1 - (-1) + 1 = 3)
    # But the problem says r - l = n, so for n=4, r - l = 4, meaning length is 5 (since r - l + 1 = length)
    # So the segment on day m should have length m + 1
    # But the sample expects r' - l' = m
    # So the segment on day m has length m + 1, but the output is l' and r' where r' - l' = m
    # Therefore, the length is m + 1, which matches the note
    # So we need to find l' and r' such that r' - l' = m, and the segment can grow to [l, r] in n - m days
    # The segment can be any [l + k, l + k + m] where k is from 0 to n - m
    # To match the sample, we can choose k such that the segment is centered or as per the sample
    # For the first test case: n=4, m=2, l=-2, r=2
    # Possible segments of length 3 (r' - l' = 2): [-2,0], [-1,1], [0,2]
    # The sample output is [-1,1], so we can choose l' = l + (n - m) // 2
    l_prime = l + (n - m) // 2
    r_prime = l_prime + m
    # Ensure the segment is within [l, r]
    if r_prime > r:
        l_prime = r - m
        r_prime = r
    print(l_prime, r_prime)