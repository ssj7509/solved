import sys
from bisect import bisect_left as l,bisect_right as r
f=lambda:map(int,sys.stdin.readline().split())
N,M,L=*f(),sorted(f())
for _ in range(M):
    i,j=f()
    print(r(L,j)-l(L,i))