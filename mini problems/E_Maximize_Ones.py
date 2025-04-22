n = int(input())
a = list(map(int, input().split()))

original_ones = sum(a)
max_gain = 0

for i in range(n):
    for j in range(i, n):
        flipped_segment = sum(1 - a[k] for k in range(i, j + 1))
        gain = original_ones + flipped_segment - sum(a[i:j + 1])
        max_gain = max(max_gain, gain)

print(max_gain)
