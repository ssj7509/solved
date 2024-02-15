N=int(input())
L,st,r=[*map(int,input().split())],[],[-1]*N
for i in range(N-1,-1,-1):
    n=L[i]
    while st:
        if st[-1]>n:
            break
        st.pop()
    if st:
        r[i]=st[-1]
    st.append(n)
print(*r)