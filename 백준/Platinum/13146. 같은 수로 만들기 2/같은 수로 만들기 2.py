import sys
f,st,m,r=sys.stdin.readline,[],0,0
for _ in range(int(f())):
    n=int(f())
    m=max(n,m)
    r+=len(st) and st[-1]<n and n-st[-1]
    while st:
        if st[-1]>n:
            break
        st.pop()
    st.append(n)
print(r+(len(st) and m-st[-1]))