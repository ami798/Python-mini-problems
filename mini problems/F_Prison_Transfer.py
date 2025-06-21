n,t,c=map(int,input () .split())
severity=list(map(int,input () .split()))
count=0
current_size=0
for sever in severity:
    if sever<=t:
        current_size+=1
    else:
        if current_size>=c:
            count+=(current_size-c+1)
            current_size=0
if current_size>=c:
    count+=(current_size-c+1)
print(count)