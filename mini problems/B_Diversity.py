s = input().strip()
k = int(input())

unique_chars = len(set(s))
n = len(s)

if k > n:
    print("impossible")
else:
    if unique_chars >= k:
        print(0)
    else:
        print(k - unique_chars)