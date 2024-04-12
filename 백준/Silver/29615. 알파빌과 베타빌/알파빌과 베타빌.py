f=lambda:map(int,input().split())
N,M,L,S,r=*f(),f(),{*f()},0
for s in (n in S for n in L):
    x=(M>0)*(1-s)
    M,r=M-s-x,r+x
print(r)