N=int(input())
L=[*map(int,input().split())]
r=[0]*N
st=[]
for i,n in enumerate(L):
    while True:
        if not st:
            break
        if st[-1][0]<n:
            st.pop()
        else:
            break
    if st:
        r[i]=st[-1][1]
    st.append((n,i+1))
print(*r)