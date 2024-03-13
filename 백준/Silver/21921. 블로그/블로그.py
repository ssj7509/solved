s,r,c,N,M,*L=0,0,0,*map(int,input().split()+input().split())
for i,n in enumerate(L):
    s+=n-(i-M>=0 and L[i-M])
    t=i>=M-1 and s>=r
    r,c=max(r,t and s),(s==r and c)+t or c
print(('SAD',f'{r}\n{c}')[r>0])