import sys,heapq as h
inp=sys.stdin.readline
def f(N):
    d=int(inp())
    q=[-int(inp())for _ in range(N-1)];h.heapify(q)
    c=0
    while True:
        m=h.heappop(q)
        if d>-m:break
        h.heappush(q,m+1)
        d+=1;c+=1
    return c
N=int(inp())
print(0 if N==1 else f(N))