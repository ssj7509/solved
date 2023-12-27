import math
def solution(numbers):
    t=int(''.join(sorted(numbers,reverse=True)))
    p={i for i in range(2,t+1)}
    base,b=p.copy(),2
    while b<=int(t**0.5):
        b=base.pop()
        for i in range(2,t//b+1):
            p.discard(b*i)
            base.discard(b*i)
    r=0
    nd={key:numbers.count(key)for key in numbers}
    for pn in p:
        s=1
        td=nd.copy()
        for n in str(pn):
            if not td.get(n) or td[n]==0:
                s=0
                continue
            td[n]-=1
        r+=s
    return r