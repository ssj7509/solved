import sys
from collections import deque
inp=sys.stdin.readline
L=list(inp().strip())
R=deque()
for i in range(int(inp())):
    a,*b=inp().split()
    if b:b=b[0]
    if a=='L' and len(L):
        R.appendleft(L.pop())
    elif a=='D' and len(R):
        L.append(R.popleft())
    elif a=='B' and len(L):
        L.pop()
    elif a=='P':
        L.append(b)
print(*L,*R,sep='')