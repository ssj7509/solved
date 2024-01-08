m,n=map(int,(input(),input()))
L=[N*N for N in range(1,101) if N*N>=m and N*N<=n];s=sum(L)
print(*(s,min(L))if s>0 else (-1,),sep='\n')