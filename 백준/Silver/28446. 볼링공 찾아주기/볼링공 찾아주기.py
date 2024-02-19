import sys
f=sys.stdin.readline
d={}
for _ in range(int(f())):
    c,*p=map(int,f().split())
    if c-1:
        print(d[p[0]])
    else:
        d[p[1]]=p[0]