import sys
f=sys.stdin.readline
for _ in range(int(f())):
    for _ in range(4):
        f()
        k1,k2,c=map(lambda s:s.split(),(f(),f(),f()))
        d={s:i for i,s in enumerate(k2)}
        print(*[c[d[k1[i]]]for i,s in enumerate(c)])