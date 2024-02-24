import sys
f=sys.stdin.readline
T=((0,1,2),(0,1,3),(0,2,3),(1,2,3))
for _ in range(int(f())):
    L,s=[*map(lambda c:(int(c[0]),c[1]),f().split())],0
    for i in T:
        t1,t2=map(lambda x:{L[y][x]for y in i},(0,1))
        if len(t2)==1 and (len(t1)==1 or (len(t1)==3 and max(t1)-min(t1)==2)):
            s=1
            break
    else:
        if len(set(L))==2 and L.count(L[0])==2:
            s=1
    print((':(',':)')[s])