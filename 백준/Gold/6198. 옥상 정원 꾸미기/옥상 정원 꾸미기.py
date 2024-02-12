import sys
f=sys.stdin.readline
st,r=[],0
for _ in range(int(f())):
    n=int(f())
    while st:
        if n>=st[-1]:
            st.pop()
        else:
            break
    r+=len(st)
    st.append(n)
print(r)