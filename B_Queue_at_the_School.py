n, t = map(int, input().split())
s = list(input())  # Convert to list for easy swapping

for _ in range(t):
    i = 0
    while i < n - 1:
        if s[i] == 'B' and s[i + 1] == 'G':
            s[i], s[i + 1] = s[i + 1], s[i]  # Swap
            i += 2  # Skip next index to avoid double swap
        else:
            i += 1

print(''.join(s))  # Convert list back to string
