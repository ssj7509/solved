N,L,st,m,s=int(input()),[*map(int,input().split())]+[-1],[],0,0
for i,n in enumerate(L):
    t=s
    while st:
        if st[-1][0]<=n:
            break
        y,t=st.pop()
        m=max(m,(s-t)*y)
    st.append((n,t))
    s+=n
print(m)