import sys
f=sys.stdin.readline
L=[0]*1000
t=0
for _ in range(int(f())):
    s,n=f().split()
    n=int(n)
    if s=="jinju":
        c=n
    if n<=1000:
        L[n-1]+=1
    else:
        t+=1
print(c)
print(sum(L[c:])+t)