N,M=map(int,input().split())
st,r=[],M
for c in input():
    n=int(c)
    while st and r:
        if st[-1]>=n:
            break
        st.pop()
        r-=1
    st.append(n)
for i in range(len(st)-r):
    print(st[i],end='')