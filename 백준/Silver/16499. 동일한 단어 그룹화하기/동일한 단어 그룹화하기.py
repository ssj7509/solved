import sys
f=sys.stdin.readline
r,st=0,set()
for _ in range(int(f())):
    k=[0]*26
    s=f().strip()
    for c in s:
        k[ord(c)-97]+=1
    st.add(tuple(k))
print(len(st))