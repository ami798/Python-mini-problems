num = int(input() .strip())
for _ in range (num):
    A,B,C = map(int,input() .split())
    if A + B ==C: 
        print("+")
    else:
        print("-")