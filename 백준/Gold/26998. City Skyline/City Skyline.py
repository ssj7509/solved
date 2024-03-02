import sys
f,st,s=sys.stdin.readline,[],0
N,M=map(int,f().split())
for i in range(N+1):
    _,n=map(int,f().split()) if i<N else (0,0)
    while st:
        if st[-1]<n:
            break
        s+=st.pop()!=n
    st.append(n)
print(s)