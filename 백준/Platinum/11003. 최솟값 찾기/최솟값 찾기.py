from collections import deque as D
N,k=map(int,input().split())
d=D()
for i,n in enumerate(map(int,input().split())):
    while d:
        if d[0][1]<i-k+1:
            d.popleft()
        elif d[-1][0]>=n:
            d.pop()
        else:
            break
    d.append((n,i))
    print(d[0][0],end=' ')