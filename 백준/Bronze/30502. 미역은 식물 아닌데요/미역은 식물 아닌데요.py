import sys
f=lambda:sys.stdin.readline().split()
n,m=map(int,f())
L=[{'P':-1,'M':-1}for _ in range(n)]
for _ in range(m):
    a,b,c=f()
    L[int(a)-1][b]=int(c)
mx,mn=0,0
for d in L:
    if d['P'] and d['M']<1:
        mx+=1
        if d['P']==1 and d['M']==0:
            mn+=1
print(mn,mx)