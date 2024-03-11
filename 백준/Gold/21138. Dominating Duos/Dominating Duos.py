import sys
f,st,r=sys.stdin.readline,[],0
for _ in range(int(f())):
    n=int(f())
    while st:
        if st[-1]>=n:
            break
        st.pop()
        r+=1
    r+=len(st) and st[-1]>n
    st.append(n)
print(r)