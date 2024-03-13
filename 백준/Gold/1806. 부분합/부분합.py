N,M,L=*map(int,input().split()),[*map(int,input().split())]
l,r,s,c,m=-1,0,L[0],1,N+1
while l<=r<N:
    if s<M:
        r+=1
        c+=r<N
        s+=r<N and L[r]
    else:
        l+=1
        m=min(m,c)
        c=c>0 and l<N and c-1
        s-=l<N and L[l]
print((m!=N+1 and m)+0)