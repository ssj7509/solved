N,L=int(input()),[*map(int,input().split())]
s,r=sum(L),0
for n in L:
    s-=n
    r+=n*s
print(r)