
t = int(input().strip())

for _ in range(t):
    
    field = [list(map(int, input().strip().split())) for _ in range(2)]

    
    num_of_cells = sum(row.count(1) for row in field)

    
    if num_of_cells == 0:
        print(0)  
    elif num_of_cells == 1 or num_of_cells == 2:
        print(1)  
    else:
        print(2)  
