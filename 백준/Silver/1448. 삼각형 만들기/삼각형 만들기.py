N,*L=map(int,open(0).read().split())
L.sort()
for i in range(N-1,1,-1):
    if L[i]<L[i-1]+L[i-2]:
        quit(print(sum(L[i-2:i+1])))
print(-1)