def f(s,t1,t2,d):
    q,p=t2-t1,t1-t2
    for i in range(len(s)-1):
        n1,n2=s[i],s[i+1]
        v=(n1==n2)+1
        t3,t4={n1-1,n2+1},{n1+1,n2-1}
        v2=not(p-{n for n in (n1,n2)if n in p and d[n]==v}) and (n1 in p)^(d[n1]>v) and (n2 in p)^(d[n2]>v)
        if v2 and ((n1>1-(i>0) and n2<9 and t3>=q and not t3-t2) or (n1<9 and n2>0 and t4>=q and not t4-t2)):
            return 1
    return 0
def g(s):
    r={}
    for n in s:
        if n not in r:
            r[n]=0
        r[n]+=1
    return r
for _ in range(3):
    a,b=map(lambda s:[*map(int,s)],input().split())
    d1,d2=map(g,(a,b))
    t1,t2=map(lambda d:{*d.keys()},(d1,d2))
    print(('friends',('nothing','almost friends')[f(a,t1,t2,d1) or f(b,t2,t1,d2)])[t1!=t2])