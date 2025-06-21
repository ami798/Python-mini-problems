def min_removal_to_palindrome(s):
    if s == s[::-1]:
        return 0

    def attempt(c):
        l, r = 0, len(s) - 1
        count = 0
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            elif s[l] == c:
                l += 1
                count += 1
            elif s[r] == c:
                r -= 1
                count += 1
            else:
                return float('inf')  # Can't fix with this letter
        return count

    res = float('inf')
    for ch in set(s):  # Only try characters that are in the string
        res = min(res, attempt(ch))

    return res if res != float('inf') else -1

# Main driver
t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    print(min_removal_to_palindrome(s))
