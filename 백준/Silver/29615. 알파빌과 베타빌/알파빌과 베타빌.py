f=lambda:map(int,input().split())
N,M,L,S=*f(),[*f()],{*f()}
t,r=len(S),0
for s in (n in S for n in L):
    x=(t>0)*(1-s)
    t,r=t-s-x,r+x
print(r)