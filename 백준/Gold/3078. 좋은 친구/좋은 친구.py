import sys
from collections import deque
f=sys.stdin.readline
def g(d,n):
    if n not in d:
        d[n]=0
    return d
n,k,d,q,r=*map(int,f().split()),{},deque(),0
t=min(n,k+1)
for _ in range(t):
    s=f().strip()
    l=len(s)
    r+=g(d,l)[l]
    d[l]+=1
    q.append(s)
for _ in range(n-t):
    s=f().strip()
    l=len(s)
    d[len(q.popleft())]-=1
    r+=g(d,l)[l]
    d[l]+=1
    q.append(s)
print(r)