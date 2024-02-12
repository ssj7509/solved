input()
L=[*map(int,input().split())]
if len(L)==1:
    r='A'
elif len(L)==2:
    r=('A',L[0])[L[0]==L[1]]
else:
    t,c=L[1]-L[0],L[2]-L[1]
    if len(set(L[1:]))==1 and L[0]!=L[1]:
        r=L[1]
    elif not t:
        r=(L[0],'B')[len(set(L))>1]
    elif c%t:
        r='B'
    else:
        a=c//t
        b,s=L[1]-L[0]*a,1
        for i in range(2,len(L)-1):
            if a*L[i]+b!=L[i+1]:
                s=0
                break
        r=('B',a*L[-1]+b)[s]
print(r)