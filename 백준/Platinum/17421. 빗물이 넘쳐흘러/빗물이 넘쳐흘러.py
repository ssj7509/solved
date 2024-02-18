N,k=map(int,input().split())
L,st,s,cs,r,m=[*map(int,input().split())]+[0],[[0,1,0]],0,0,0,0
for n in L:
    if st[-1][0]<=n:
        if cs==k-1 and st[-1][0]<n:
            m=k
            break
        st.append([n,1,0])
    else:
        c=1
        cs+=1
        while True:
            if st[-1][0]<=n:
                break
            t=st.pop()
            c+=t[1]
            s+=(t[0]-n)*t[1]
            cs-=t[2]
        m=max(m,cs)
        st.append([n,c,1])
        if cs==k-1:
            r=s
print((-1,r)[m>=k])