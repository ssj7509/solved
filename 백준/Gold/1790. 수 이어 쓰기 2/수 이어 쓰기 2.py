n,k=map(int,input().split())
c,l,p=0,0,0
while True:
    tc=c+9*10**p
    tl=l+(p+1)*9*10**p
    if tl>=k:
        q,r=divmod(k-l,p+1)
        print(str(10**p+q+bool(r)-1)[(r-1)%(p+1)]if n>=c+q+bool(r) else -1)
        break
    c,l,p=tc,tl,p+1