from collections import deque
N,d=int(input()),deque(enumerate(map(int,input().split())))
for _ in range(N):
    n=print(d[0][0]+1,end=' ')or d[0][1]
    _=d.popleft(),[d.rotate((n>0)-n)]