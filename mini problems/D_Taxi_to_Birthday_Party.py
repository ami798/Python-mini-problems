n=int(input())
grp=list(map(int,input().split()))
one=grp.count(1)
two=grp.count(2)
three=grp.count(3)
four=grp.count(4)
taxi=four
taxi+=three
one=max(0,one - three)
taxi+=two//2
if two %2 !=0:
    taxi+=1
    one=max(0,one-2)
    taxi+=(one+3)//4
print(taxi)