import sys,heapq as H
f,h=sys.stdin.readline,[]
for _ in range(int(f())):
    n=int(f())
    if n:
        H.heappush(h,n)
    else:
        print(len(h) and H.heappop(h))