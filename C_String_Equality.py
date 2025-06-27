from collections import Counter
import sys
input = sys.stdin.read

def can_transform(n, k, a, b):
    count_a = [0] * 26
    count_b = [0] * 26

    for ch in a:
        count_a[ord(ch) - ord('a')] += 1
    for ch in b:
        count_b[ord(ch) - ord('a')] += 1

    for i in range(25):  # from 'a' to 'y'
        if count_a[i] < count_b[i]:
            return "No"
        extra = count_a[i] - count_b[i]
        if extra % k != 0:
            return "No"
        count_a[i + 1] += extra  # push extra to next char

    return "Yes" if count_a[25] == count_b[25] else "No"

# Handle multiple test cases
data = input().split()
t = int(data[0])
idx = 1
results = []

for _ in range(t):
    n = int(data[idx])
    k = int(data[idx + 1])
    a = data[idx + 2]
    b = data[idx + 3]
    results.append(can_transform(n, k, a, b))
    idx += 4

print("\n".join(results))
