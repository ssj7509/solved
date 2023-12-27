def solution(park, routes):
    d={'E':(0,1),'W':(0,-1),'S':(1,0),'N':(-1,0)}
    for i,row in enumerate(park):
        t=0
        for j,c in enumerate(row):
            if c=='S':
                t=1
                s=[i,j]
                break
        if t:
            break
    h,w=len(park),len(park[0])
    for c in routes:
        v,n=c.split();n=int(n)
        rv,cv=d[v]
        if any((s[0]+n*rv<0,s[0]+n*rv>=h,s[1]+n*cv<0,s[1]+n*cv>=w)):
            continue
        t=0
        for i in range(1,n+1):
            if park[s[0]+i*rv][s[1]+i*cv]=='X':
                t=1
                break
        if t:
            continue
        s[0]+=rv*n
        s[1]+=cv*n
    return s
