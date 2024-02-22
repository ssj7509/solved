N,k,L,st,m=*map(int,input().split()),[*map(int,input().split())],[],0
for n in L:
    while st:
        if st[-1]>n:
            break
        st.pop()
    if n<k:
        st.append(n)
    m=max(m,len(st))
print(m)