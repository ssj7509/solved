def f(L,st,r,m):
    for i,n in enumerate(L):
        j=(i,len(L)-i-1)[m]
        while st:
            if st[-1][0]<=n:
                st.pop()
            else:
                break
        if st:
            r[j][0]+=len(st)
            r[j][1].append(st[-1][1])
        st.append([n,j+1])    
N=int(input())
L=[*map(int,input().split())]
st,r=[],[[0,[]]for _ in range(N)]
f(L,st,r,0)
st.clear()
f(L[::-1],st,r,1)
for i,n in enumerate(r):
    print(*(n[0],sorted(n[1],key=lambda x:(abs(i+1-x),x))[0])if n[0]>0 else (0,))