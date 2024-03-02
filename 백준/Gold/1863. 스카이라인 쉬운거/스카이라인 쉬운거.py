import sys
f=sys.stdin.readline
N,st,s=int(f()),[],0
for i in range(N+1):
    _,n=map(int,f().split()) if i<N else (0,0)
    while st:
        if st[-1]<n:
            break
        s+=st.pop()!=n
    st.append(n)
print(s)