import sys
from bisect import bisect_left as l
f=sys.stdin.readline
N,M=map(int,f().split())
L=sorted(int(f())for _ in range(N))
for _ in range(M):
    n=int(f())
    t=l(L,n)
    print((-1,t)[t<N and L[t]==n])