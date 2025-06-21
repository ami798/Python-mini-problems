t=input()
n=len(t)
for overlap in range(1,n):
    c=t[:n-overlap]
    if c + c[overlap:] ==t:
        print("YES")
        print(c)
        break
else:
    print("NO")