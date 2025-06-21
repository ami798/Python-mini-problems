t = int(input())
for _ in range(t):
    
    n, k = map(int, input().split())
    s = input()
    white_count = s[:k].count('W')

   
    min_col = white_count
    for i in range(k, n):
       
        if s[i - k] == 'W':
            white_count -= 1
        if s[i] == 'W':
            white_count += 1

        min_col = min(min_col, white_count)

    print(min_col)