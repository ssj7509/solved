N=int(input())
L,st,r=[*map(int,input().split())],[],[0]*N
for i,n in enumerate(L):
    while st:
        if st[-1][0]<n:
            break
        st.pop()
    if st:
        r[i]=st[-1][1]
    st.append((n,i+1))
print(*r)