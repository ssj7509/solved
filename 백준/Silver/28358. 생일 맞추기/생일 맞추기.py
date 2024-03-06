import sys
f,T=sys.stdin.readline,{1,3,5,7,8,10,12}
for _ in range(int(f())):
    s,r=set(str(i) for i,n in enumerate(f().split()) if n=='0'),0
    for m in set(n for n in range(1,13) if set(str(n))<=s):
        r+=len(set(d for d in range(1,(31,30,32)[2*(m in T)+(m==2)]) if set(str(d))<=s))
    print(r)