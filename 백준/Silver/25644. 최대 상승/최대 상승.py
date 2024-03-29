_,m,r=input(),10**9,0
for n in map(int,input().split()):
    r,m=max(r,n-m),min(n,m)
print(r)