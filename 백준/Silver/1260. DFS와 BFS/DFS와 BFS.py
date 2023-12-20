import sys
inp=sys.stdin.readline
sys.setrecursionlimit(20000)
def f1(N,g,v,r):
    if v[N]:
        return
    v[N]+=1
    r.append(N+1)
    for n in g[N]:
        f1(n,g,v,r)
def f2(g,v,r,q):
    while q:
        N=q[0]
        del q[0]
        if v[N]:continue
        v[N]=1
        r.append(N+1)
        for n in g[N]:
            if not v[n]:
                q.append(n)
n,m,s=map(int,inp().split())
g=[[]for _ in range(n)]
r1,r2=[],[]
for i in range(m):
    a,b=map(int,inp().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
for i in range(n):
    g[i].sort()
f1(s-1,g,[0]*n,r1)
f2(g,[0]*n,r2,[s-1])
print(*r1,sep=' ')
print(*r2,sep=' ')