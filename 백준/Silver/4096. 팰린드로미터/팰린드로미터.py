import sys
def f(NL,l,r,t):
    n=g(NL,l,r,t)
    NL[l-n]+=1
    h(NL,l,r,t,n)
def g(NL,l,r,t):
    for i in range(t):
        if NL[l-i]!=9:
           return i
        else:
            NL[l-i]=NL[r+i]=0
def h(NL,l,r,t,n):
    for i in range(t-n):
        NL[r+n+i]=NL[l-n-i]
while True:
    N=sys.stdin.readline().strip()
    if N=='0':
        break
    NL=list(map(int,N))
    r,m=divmod(len(NL),2)
    l=r+m-1
    t=l+1
    for i in range(t):
        if NL[l-i]>NL[r+i]:
            NL[r+i]=NL[l-i]
            h(NL,l,r,t,i)
        elif NL[l-i]<NL[r+i]:
            f(NL,l,r,t)
            break
    print(int(''.join(map(str,NL)))-int(N))