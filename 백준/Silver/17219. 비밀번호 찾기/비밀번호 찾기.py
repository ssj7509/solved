import sys
f=lambda:sys.stdin.readline().split()
N,M=map(int,f())
d=dict(f() for _ in range(N))
for _ in range(M):
    print(d[f()[0]])