t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    
    zeros = s.count('0')
    ones = s.count('1')
    
    total_pairs = n // 2
    bad_pairs = total_pairs - k


    if bad_pairs > min(zeros, ones):
        print("NO")
        continue

    
    remaining_zeros = zeros - bad_pairs
    remaining_ones = ones - bad_pairs

    good_pairs_possible = (remaining_zeros // 2) + (remaining_ones // 2)

    if good_pairs_possible >= k:
        print("YES")
    else:
        print("NO")
