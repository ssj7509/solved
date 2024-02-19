N,L,d,st=int(input()),[*map(int,input().split())],{},[]
r=[-1]*N
for n in L:
    if n not in d:
        d[n]=0
    d[n]+=1
for i in range(N-1,-1,-1):
    n=L[i]
    while st:
        if st[-1][1]>d[n]:
            break
        st.pop()
    if st:
        r[i]=st[-1][0]
    st.append((n,d[n]))
print(*r)