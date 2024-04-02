import sys
from bisect import bisect_left as l,bisect_right as r
f=lambda:map(int,sys.stdin.readline().split())
N,M,L=*f(),sorted(f())
for _ in range(M):
    c,*t=f()
    i,j=t[0],t[c>2]
    print((N-l(L,i),N-l(L,i+1),r(L,j)-l(L,i))[c-1])