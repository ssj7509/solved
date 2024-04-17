from bisect import bisect_right as b
N,*L=map(int,open(0).read().split())
L.sort()
print(sum(b(L,10*L[i]/9,i+1)-i-1 for i in range(N)))