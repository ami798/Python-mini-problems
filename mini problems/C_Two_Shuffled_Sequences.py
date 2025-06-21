from collections import Counter

# Read input
n = int(input())
a = list(map(int, input().split()))

# Count frequency of each number
freq = Counter()
for num in a:
    freq[num] += 1
    if freq[num] > 2:
        print("NO")
        exit()

# Separate into increasing and decreasing
increasing = []
decreasing = []

for num in sorted(freq.keys()):
    increasing.append(num)
    if freq[num] == 2:
        decreasing.append(num)

# Sort decreasing in reverse order
decreasing.sort(reverse=True)

# Output result
print("YES")
print(len(increasing))
print(' '.join(map(str, increasing)))
print(len(decreasing))
print(' '.join(map(str, decreasing)))
