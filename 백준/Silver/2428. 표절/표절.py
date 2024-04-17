from bisect import bisect_right as b
_,*L=map(int,open(0).read().split())
L.sort()
print(sum(b(L,10*n/9,i+1)-i-1 for i,n in enumerate(L)))