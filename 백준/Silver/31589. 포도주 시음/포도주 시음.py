N,K,*L=map(int,open(0).read().split())
L.sort()
print(sum(L[-((K+1)//2):])-sum(L[:(K+1)//2-1]))