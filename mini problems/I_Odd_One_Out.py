num = int(input() .strip())
for _ in range (num):
    A,B,C = map(int,input() .split())
    if A == B :
        print(C)
    elif A==C :
        print(B)
    elif B == C:
        print(A)