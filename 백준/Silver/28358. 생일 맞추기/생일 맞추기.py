import sys
f,T=sys.stdin.readline,[31,29,31,30,31,30,31,31,30,31,30,31]
for _ in range(int(f())):
    s,r=set(str(i) for i,n in enumerate(f().split()) if n=='0'),0
    for m in (n for n in range(1,13) if set(str(n))<=s):
        r+=len([d for d in range(1,T[m-1]+1) if set(str(d))<=s])
    print(r)