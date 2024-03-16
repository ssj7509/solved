N,L=int(input()),sorted(map(int,input().split()))
s1,s2,r=0,sum(L),-1
m=s2+1
for i,n in enumerate(L):
    t,s1,s2=min(m,n*i-s1+s2-n*(N-i)),s1+n,s2-n
    m,r=((m,r),(t,n))[t<m]
print(r)