N=int(input())
L1,L2,s=[],[],0
for n in input().split():
    t=int(n)
    L1.append(t)
    if t%2==1:L2.append(t)
    s+=t
if s%2==1:
    s-=min(L2)
print(s)
