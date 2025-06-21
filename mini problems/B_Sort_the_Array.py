n = int(input())
a = list(map(int, input().split()))

b = sorted(a)


l, r = 0, n - 1
while l < n and a[l] == b[l]:
    l += 1
while r >= 0 and a[r] == b[r]:
    r -= 1


if l > r:
    print("yes")
    print(1, 1)  
else:
    
    a[l:r+1] = a[l:r+1][::-1]
    if a == b:
        print("yes")
        print(l + 1, r + 1)  
    else:
        print("no")
