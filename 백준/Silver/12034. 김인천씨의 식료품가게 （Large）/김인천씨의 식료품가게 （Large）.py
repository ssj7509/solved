import sys
f=sys.stdin.readline
for i in range(int(f())):
    n=int(f())
    L,d=[*map(int,f().split())],{}
    for p in L:
        if p not in d:
            d[p]=0
        d[p]+=1
    r=[]
    for p in L[::-1]:
        k=p//4*3
        if d[p] and p%4==0 and k in d and d[k]:
            r.append(k)
            d[p]-=1
            d[k]-=1
    print(f"Case #{i+1}:",*sorted(r))