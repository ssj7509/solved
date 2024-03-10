N,M,L=*map(int,input().split()),[*map(int,input().split())]
l,r,s,c=-1,0,L[0],0
while l<=r<N:
    c+=s==M
    if s<M:
        r+=1
        s+=r<N and L[r]
    else:
        l+=1
        s-=l<N and L[l]
print(c)