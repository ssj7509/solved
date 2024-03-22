m,N,*L=map(int,['0',input()]+input().split())
s=L[0]
for n in L:
    s=min(s,n)
    m=max(m,n-s)
    print(m,end=' ')