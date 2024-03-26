s,m,N,K,*L=0,0,*map(int,(input()+' '+input()).split())
for i in range(N*2):
    s+=L[i%N]-(i>=K and L[(i-K)%N])
    m=max(s,m)
print(m)