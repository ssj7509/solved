import sys
f=lambda:map(int,sys.stdin.readline().split())
n,m=f()
nL=[[*sorted(f())]for _ in range(n)]
mxL=[max(L[i] for L in nL)for i in range(m)]
cL=[len([i for i in range(m)if L[i]==mxL[i]])for L in nL]
mx=max(cL)
print(*[i+1 for i,n in enumerate(cL)if n==mx])