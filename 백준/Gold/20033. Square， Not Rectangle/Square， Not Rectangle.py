import sys
f=sys.stdin.readline
N,st,m,lx=int(f()),[],0,-1
L=[*map(int,f().split())]
for i,n in enumerate(L):
    while st:
        if st[-1][1]>n:
            x,y=st.pop()
            m,lx=max(m,min(i-x,y)),x
        else:
            break
    if not st or st and (st[-1][1]<n):
        st.append(((i,lx)[lx>-1],n))
    lx=-1
while st:
    x,y=st.pop()
    m=max(m,min(N-x,y))
print(m)