import sys
inp=sys.stdin.readline
N,M=map(int,inp().split())
S={inp()for _ in range(N)}
r=0
for i in range(M):
    if inp() in S:
        r+=1
print(r)