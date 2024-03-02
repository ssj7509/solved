N,L,s,c,r=int(input()),[*map(int,input().split())],0,1,1
for i in range(N-1):
    n,m=L[i],L[i+1]
    t,c=n>m,c+1
    if s&(1-t) or n==m:
        c=(n!=m)+1
    r,s=max(r,c),t
print(r)