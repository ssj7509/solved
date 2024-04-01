import sys
f=lambda:map(int,sys.stdin.readline().split())
N,M,*L=*f(),*f()
s,a=0,[0]*N
for i,n in enumerate(sorted(L)):
    s+=n
    a[i]=s
for _ in range(M):
    l,r=f()
    print(a[r-1]-(l>1 and a[l-2]))