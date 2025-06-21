t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if n == 2:
        print("Yes")
        continue
    
    all_same = True
    first = a[0]
    for num in a[1:]:
        if num != first:
            all_same = False
            break
    if all_same:
        print("Yes")
        continue
    

    unique_elements = list(set(a))
    if len(unique_elements) != 2:
        print("No")
        continue
    x, y = unique_elements
    count_x = a.count(x)
    count_y = a.count(y)
    

    if (n % 2 == 0 and count_x == count_y) or (n % 2 == 1 and abs(count_x - count_y) == 1):
        print("Yes")
    else:
        print("No")