import sys
f=sys.stdin.readline
d,d2,r={},{},"Not Delicious..."
for _ in range(int(f())):
    k,v=f().split()
    v=int(v)
    if k not in d:
        d[k]=0
    d[k]+=v
for k in d:
    n=d[k]
    if n not in d2:
        d2[n]=0
    d2[n]+=1
for k in d2:
    t=k*1618//1000
    if t in d2 and ((t==k and d2[k]>1) or t!=k):
        r="Delicious!"
        break
print(r)