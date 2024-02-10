from collections import deque
import sys
f=sys.stdin.readline
d,m,i=deque(),0,0
for _ in range(int(f())):
    n=[*map(int,f().split())]
    if n[0]==1:
        d.append(n[1])
        if len(d)>m:
            m,i=len(d),n[1]
        elif len(d)==m:
            i=min(i,n[1])
    elif n[0]==2:
        d.popleft()
print(m,i)