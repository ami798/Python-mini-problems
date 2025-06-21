n = int(input())
a = list(map(int, input().split()))
a.sort()

max_team = 1
left = 0

for right in range(n):
    while a[right] - a[left] > 5:
        left += 1
    max_team = max(max_team, right - left + 1)

print(max_team)