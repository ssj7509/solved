import sys
inp=sys.stdin.readline
T=int(inp())
for i in range(T):
    d={}
    for j in range(int(inp())):
        _,c=inp().split()
        if d.get(c):d[c]+=1
        else:d[c]=1
    r=1
    for j in d:
        r*=d[j]+1
    print(r-1)