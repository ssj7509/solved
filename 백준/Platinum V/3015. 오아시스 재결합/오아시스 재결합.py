import sys
f=sys.stdin.readline
st,r=[],0
for _ in range(int(f())):
    n,t=int(f()),1
    while st:
        if st[-1][0]<n:
            st.pop()
            r+=1
        else:
            break
    if st:
        if st[-1][0]==n:
            r+=st[-1][1]+(len(st)-st[-1][1]>0)
            t=st[-1][1]+1
        else:
            r+=1
    st.append((n,t))
print(r)