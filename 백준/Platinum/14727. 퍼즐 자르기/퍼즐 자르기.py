import sys
f=sys.stdin.readline
st,m,lx=[],0,-1
N=int(f())
for i in range(N):
    n=int(f())
    while st:
        if st[-1][1]>n:
            x,y=st.pop()
            m,lx=max(m,(i-x)*y),x
        else:
            break
    if not st or st and (st[-1][1]<n):
        st.append(((i,lx)[lx>-1],n))
    lx=-1
while st:
    x,y=st.pop()
    m=max(m,(N-x)*y)
print(m)