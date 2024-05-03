L=[*map(int,open(0).read().split())]
m=max(L)
i,j=divmod(L.index(m),9)
print(m)
print(i+1,j+1)