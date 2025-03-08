num = int(input() .strip())
for _ in range (num):
    A,B,C = map(int,input() .split())
    if A + B >=10 or A + C >= 10 or B + C >=10: 
        print("YES")
    else:
        print("NO")