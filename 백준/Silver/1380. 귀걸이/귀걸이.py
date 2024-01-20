import sys
f=sys.stdin.readline
t,rL=1,[]
while True:
    n=int(f())
    if n==0:
        break
    sL,cL=[f().strip()for _ in range(n)],[0]*n
    for _ in range(2*n-1):
        i,_=f().split();i=int(i)-1
        cL[i]+=1
    rL+=[f"{t} {sL[i]}"for i,c in enumerate(cL) if c==1]
    t+=1
print(*rL,sep='\n')