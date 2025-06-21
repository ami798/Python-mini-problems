n = int(input())

if n == 1 or n == 2:
    print(-1)
else:
    if n % 2 == 1:  # n is odd
        m = (n**2 - 1) // 2
        k = (n**2 + 1) // 2
    else:  # n is even
        m = (n // 2)**2 - 1
        k = (n // 2)**2 + 1
    print(m, k)