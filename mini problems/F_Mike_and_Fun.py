def consecutive_one(row):# to represent the row
    high_value = 0#to start with 0
    now = 0
    for value in row:
        if value == 1:
            now+= 1
            if now > high_value:
                high_value = now
        else:
            now = 0
    return high_value
x,y,z = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(x)]
rounds = [tuple(map(int, input().split())) for _ in range(z)]

for a,b in rounds:
    a -= 1
    b-= 1
    matrix[a][b] = 1 - matrix[a][b]#to represent the 2 by 2 matrices
    
    
    highest_score = 0
    for row in matrix:
        highest_score = max(highest_score, consecutive_one(row))
    
    
    print(highest_score) , end = ''