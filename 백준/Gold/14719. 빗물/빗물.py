input()
L,st,m,r=[*map(int,input().split())],[],0,0
for n in L:
    if not st or (st and st[-1][0]>=n):
        st.append((n,1))
    else:
        c=1
        while st:
            if st[-1][0]>=n:
                break
            t,l=st.pop()
            r+=(min(m,n)-t)*l
            c+=l
        st.append((n,c))
    m=max(m,n)
print(r)