t=int(input())

for _ in range(t):
    a=input().strip()
    b=''
    for char in reversed(a):
        if char=='p':
            b+='q'
        elif char =='q':
            b+='p'
        elif char=='w':
            b+='w'
    print(b)
    