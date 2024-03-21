m,N,*L=map(int,['0',input()]+input().split())
b=s=L[0]
for n in L:
    t=n>=s
    b,s=t and max(b,n),(n,s)[t]
    m=max(m,b-s)
    print(m,end=' ')