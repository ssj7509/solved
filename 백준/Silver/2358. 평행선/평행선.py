import sys
f=sys.stdin.readline
xd,yd={},{}
for _ in range(int(f())):
    x,y=map(int,f().split())
    if x not in xd:xd[x]=0
    if y not in yd:yd[y]=0
    xd[x]+=1;yd[y]+=1
print(sum(map(lambda d:len([k for k,v in d.items() if v>=2]),(xd,yd))))