import sys
f=sys.stdin.readline
N,M,b=*map(int,f().split()),int(f())
for _ in range(N-1):
    n=int(f())
    M+=b<n and (n-b)*(M//b)
    b=n
print(M)