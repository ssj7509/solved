N,M,L,s,r,c=*map(int,input().split()),[*map(int,input().split())],0,0,0
for i,n in enumerate(L):
    s+=n
    s-=i-M>=0 and L[i-M]
    t=i>=M-1 and s>=r
    r,c=max(r,t and s),(s==r and c)+t or c
print(*(('SAD',),(r,c))[r>0],sep='\n')