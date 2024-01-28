def f(L):
    r=1
    for n in L:
        r*=n
    return r
N=int(input())
L=[*map(int,input().split())]
s=0
for i in range(1,N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            s=max(s,sum(map(f,(L[:i],L[i:j],L[j:k],L[k:]))))
print(s)