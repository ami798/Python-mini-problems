s=input()
st=[]
for c in s:
    if st and st[-1]==c:
        st.pop()
    else:
        st.append(c)
print(''.join(st))