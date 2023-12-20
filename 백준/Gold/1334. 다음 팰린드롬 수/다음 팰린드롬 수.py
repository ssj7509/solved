NL=list(map(int,input()))
def f(NL,l,r,t):
    n=g(NL,l,r,t)
    if n==-1:
        NL.insert(0,1)
        NL[-1]=1
        return
    NL[l-n]+=1
    h(NL,l,r,t,n)
def g(NL,l,r,t):
    for i in range(t):
        if NL[l-i]!=9:
           return i
        else:
            NL[l-i]=NL[r+i]=0
    return -1
def h(NL,l,r,t,n):
    for i in range(t-n):
        NL[r+n+i]=NL[l-n-i]
r=len(NL)//2
l=r+len(NL)%2-1
t=l+1
s=1
for i in range(t):
    if NL[l-i]>NL[r+i]:
        NL[r+i]=NL[l-i]
        h(NL,l,r,t,i)
        s=0
    elif NL[l-i]<NL[r+i]:
        f(NL,l,r,t)
        s=0
        break
if s:
    f(NL,l,r,t)
print(*NL,sep='')
