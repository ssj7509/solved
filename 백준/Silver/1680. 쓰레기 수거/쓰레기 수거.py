import sys
f=sys.stdin.readline
for _ in range(int(f())):
    w,n=map(int,f().split())
    t,r,bx=0,0,0
    for _ in range(n):
        x,ww=map(int,f().split())
        r+=x-bx
        t,r,bx=((t+ww,r,x),(0,r+x,0),(ww,r+2*x,x))[(t+ww>=w)+(t+ww>w)]
    r+=bx
    print(r)