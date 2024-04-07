r,N,M=1,*map(int,input().split())
if N<M:
    for i in range(2,N+1):
        r=r*i%M
    print(r)
else:
    print(0)