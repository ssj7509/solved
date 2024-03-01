import sys
f=sys.stdin.readline
N,M=map(int,f().split())
st,m,r=[],0,0
for _ in range(N):
    n=int(f())
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