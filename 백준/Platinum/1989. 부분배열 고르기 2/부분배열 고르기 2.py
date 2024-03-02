N,L,st,m,s,l,r=int(input()),[*map(int,input().split())]+[-1],[],0,0,1,1
for i,n in enumerate(L):
    x,t=i,s
    while st:
        if st[-1][0]<=n:
            break
        y,x,t=st.pop()
        tm=max(m,(s-t)*y)
        if tm>m:
            m,l,r=tm,x+1,i
    st.append((n,x,t))
    s+=n
print(m)
print(l,r)