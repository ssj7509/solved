import sys
f=sys.stdin.readline
while True:
    st,m,lx=[],0,-1
    L=[*map(int,f().split())]
    if L==[0]:
        break
    N=L[0]
    for i,n in enumerate(L[1:]):
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