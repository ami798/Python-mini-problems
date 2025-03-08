peoples = int(input().strip())
for _ in range(peoples):
    
    n, r = map(int, input().split().split)
    
    num_of_families = list(map(int, input().split()))
    
    happy_peo = 0
    singles = 0
    
    for family in num_of_families:
        if family >= 2:
            happy_peo += 2
        else:
            happy_peo += 1
    
    print(happy_peo)


    t = int(input().strip())

for _ in range(t):
    n, r = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))

    count = 0
    singles = 0
    for i in range(n):
        count += (arr[i] // 2) * 2
        arr[i] = arr[i] % 2
        if arr[i] == 1:
            singles += 1

    left_rows = r - count // 2
    if left_rows > singles:
        print(count + singles)
        continue
    else:
        print(count + (left_rows * 2 - singles))
