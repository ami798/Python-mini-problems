num = int(input() .strip())
for _ in range (num):
    A,B,C = map(int,input() .split())
    if A + B == C or A + C ==B or C + B== A:
        print("YES")
    else:
        print("NO")