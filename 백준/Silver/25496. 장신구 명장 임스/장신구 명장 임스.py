import sys
f=sys.stdin.readline
r,N,M,*L=0,*map(int,(f()+' '+f()).split())
for n in sorted(L):
    if N>=200:
        break
    r+=1
    N+=n
print(r)