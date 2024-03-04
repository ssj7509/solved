from collections import deque as D
import sys
f,V=sys.stdin.readline,((0,1),(1,0),(0,-1),(-1,0))
N=int(f())
L,D=[[0]*N for _ in range(N)],D([(0,0)])
for _ in range(int(f())):
    n,m=map(int,f().split())
    L[n-1][m-1]=1
T,L[0][0],v,r=int(f()),2,0,0
for i in range(T+1):
    x,c=i<T and f().split() or (100,'D')
    n,m,vn,vm=*D[0],*V[v]
    for j in range(1,int(x)-r+1):
        tn,tm,r=n+vn*j,m+vm*j,r+1
        if not (0<=tn<N and 0<=tm<N and L[tn][tm]<2):
            print(r)
            quit()
        D.appendleft((tn,tm))
        if L[tn][tm]:
            L[tn][tm]=2
            continue
        L[tn][tm]=2
        pn,pm=D.pop()
        L[pn][pm]=0
    v=(v+1,v-1)[c=='L']%4