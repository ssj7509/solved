import sys
from collections import deque
f,d=sys.stdin.readline,deque()
for _ in range(int(f())):
    c,*n=f().split()
    if c=='push':
        d.append(int(n[0]))
    elif c=='pop':
        print(len(d) and d.popleft() or -1)
    elif c=='size':
        print(len(d))
    elif c=='empty':
        print(1-(len(d) and 1))
    elif c=='front':
        print(len(d) and d[0] or -1)
    else:
        print(len(d) and d[-1] or -1)