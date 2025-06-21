t = int(input())
for _ in range(t):
    n = int(input())
    found = False
    for i in range(1, 27):  # first letter
        for j in range(1, 27):  # second letter
            k = n - i - j  # third letter
            if 1 <= k <= 26:
                # Convert numbers to letters
                word = chr(ord('a') + i - 1) + chr(ord('a') + j - 1) + chr(ord('a') + k - 1)
                print(word)
                found = True
                break
        if found:
            break
