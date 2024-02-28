import sys
f=sys.stdin.readline
S=[-1]*int(f())
L=[*map(int,f().split())]
r=sum(L)
print(r)
for _ in range(int(f())):
    c,*t=map(int,f().split())
    if c-1:
        i=t[0]-1
        r+=S[i]*L[i]
        S[i]*=-1
    else:
        i,x=t
        r-=(L[i-1]-x)*(S[i-1]<0)
        L[i-1]=x
    print(r)