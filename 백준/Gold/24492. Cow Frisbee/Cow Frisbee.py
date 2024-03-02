input()
L,st,r=[*map(int,input().split())],[],0
for i,n in enumerate(L):
    while st:
        if st[-1][0]>=n:
            break
        else:
            t,x=st.pop()
            r+=i-x+1
    if st:
        r+=i-st[-1][1]+1
    st.append((n,i))
print(r)