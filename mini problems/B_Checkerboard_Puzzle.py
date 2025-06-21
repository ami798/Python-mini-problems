
n = int(input())  
board = [input().strip() for _ in range(n)]


def is_valid_checkerboard(n, board):
    for i in range(n):
        for j in range(n):
            
            adjacent_count = 0
            
            
            if i > 0 and board[i-1][j] == 'o':  
                adjacent_count += 1
            if i < n-1 and board[i+1][j] == 'o': 
                adjacent_count += 1
            if j > 0 and board[i][j-1] == 'o':  
                adjacent_count += 1
            if j < n-1 and board[i][j+1] == 'o':  
                adjacent_count += 1
            if adjacent_count % 2 != 0:
                return "NO"
    return "YES"


print(is_valid_checkerboard(n, board))
