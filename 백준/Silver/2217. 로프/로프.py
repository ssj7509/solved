import sys
N=int(input())
nL=sorted([int(sys.stdin.readline()) for _ in range(N)])
maxN=0
for i in range(N):
    if nL[i]*(N-i)>maxN:
        maxN=nL[i]*(N-i)
print(maxN)
