t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    max_char = max(s)
    alphabet_size = ord(max_char) - ord('a') + 1
    print(alphabet_size)