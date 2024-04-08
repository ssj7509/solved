m,r,N,*L=0,-1,*map(int,[input()]+input().split())
L.sort()
for i in range(N-1):
    t=max(m,(L[i+1]-L[i])//2)
    r,m=((L[i]+L[i+1])//2,t) if m<t else (r,m)
print(r)