import sys
f=lambda:map(int,sys.stdin.readline().split())
N,M=f()
L,s=[0]*N,0
for i,n in enumerate(f()):
    s+=n
    L[i]=s
for _ in range(M):
    i,j=f()
    print(L[j-1]-(i-2>=0 and L[i-2]))