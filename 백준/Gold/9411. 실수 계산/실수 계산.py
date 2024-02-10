import sys
from decimal import Decimal as D,getcontext
getcontext().prec=1000
f=sys.stdin.readline
def g(d):
    s=h(d)
    i=s.find('.')
    j=s[0]=='-'
    return D(s[:30+(i>-1 and i<30+j)+(s[0]=='-')])
def h(d):
    return format((d.to_integral(),d.normalize())[d!=r.to_integral()],'f')
for _ in range(int(f())):
    r=D(0)
    while True:
        t=g(D(f()))
        if t==0:
            break
        r=g(r+t)
    print(h(r))