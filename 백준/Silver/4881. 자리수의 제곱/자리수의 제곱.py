import sys
def f(n):
    d,t,i={},n,0
    while True:
        if t in d:
            break
        d[t]=i
        t=sum(int(c)**2 for c in str(t))
        i+=1
    return d
while True:
    a,b=map(int,sys.stdin.readline().split())
    if a+b==0:
        break
    ad,bd=f(a),f(b)
    r,m=0,[]
    for n in ad:
        if n in bd:
            m.append(ad[n]+bd[n]+2)
    if m:
        r=min(m)
    print(a,b,r)