from collections import deque as D
N,m,c=map(int,input().split())
d1,d2,s=D(),D(),1
for i,n in enumerate(map(int,input().split())):
    while d1:
        if d1[0][1]<i-m+1:
            d1.popleft()
        elif d1[-1][0]>=n:
            d1.pop()
        else:
            break
    while d2:
        if d2[0][1]<i-m+1:
            d2.popleft()
        elif d2[-1][0]<=n:
            d2.pop()
        else:
            break
    d1.append((n,i))
    d2.append((n,i))
    if i>=m-1 and d2[0][0]-d1[0][0]<=c:
        print(i-m+2)
        s=0
if s:
    print("NONE")