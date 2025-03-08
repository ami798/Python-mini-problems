n, m = map(int, input().split())

if n > m + 1 or m > 2 * (n + 1):
    print(-1)
else:
    if n == m:
        print("10" * n)
    elif n == m + 1:
        print("10" * n + "1")
    else:
        result = ['1', '0'] * n
        result.append('1')
        m -= n + 1
        i = 0

        while m > 0:
            result[i] = '11'
            m -= 1
            i += 2
        
        print(''.join(result))
