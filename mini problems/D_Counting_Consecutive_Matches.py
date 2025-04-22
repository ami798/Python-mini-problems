s = input().strip()
n = len(s)
m = int(input())

prefix = [0] * (n + 1)

for i in range(1, n):
    prefix[i+1] = prefix[i] + (1 if s[i-1] == s[i] else 0)

output = []
for _ in range(m):
    l, r = map(int, input().split())
    output.append(str(prefix[r] - prefix[l]))

print('\n'.join(output))