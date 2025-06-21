
n = int(input())
current_pass= 0
max_pass = 0


for _ in range(n):
    a, b = map(int, input().split())
    current_pass -= a  
    current_pass += b  
    if current_pass > max_pass:
        max_pass = current_pass 


print(max_pass)
