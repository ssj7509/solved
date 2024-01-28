import sys
f=sys.stdin.readline
d,r={},0
for _ in range(int(f())):
    a,b=map(int,f().split())
    if a not in d:
        d[a]=0
    if d[a]==b:
        r+=1
    r+=b-d[a]
    d[a]=b
print(r)