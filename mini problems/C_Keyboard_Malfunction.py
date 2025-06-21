t=int(input())
for _ in range(t):
    s=input().strip()
    working_buttons=set()
    i=0
    while i<len(s):
        if i+1<len(s) and s[i]==s[i+1]:
            i+=2
        else:
            working_buttons.add(s[i])
            i+=1
    sorted_one=sorted(working_buttons)
    if sorted_one:
        print("".join(sorted(working_buttons)))
    else:
        print()
