import sys
inp=sys.stdin.readline
N,l=map(int,inp().split())
t=p=0
for _ in range(N):
    D,R,G=map(int,inp().split())
    t+=D-p
    p+=D-p
    s=t%(R+G)
    if s<R:
        t+=R-s
print(t+l-p)