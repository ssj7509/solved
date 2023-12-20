M,N=map(int,input().split())
nL=[i for i in range(M,N+1)]
pL=[0]*int(N**0.5)
base=2
while base<=int(N**0.5):
    if not pL[base-2]:
        if M+(base-M%base)%base!=base:
            nL[(base-M%base)%base]=0
        for i in range(1,N//base-(M-1)//base):
            nL[(base-M%base)%base+base*i]=0
        for i in range((len(pL))//base):
            pL[base-2+base*i]=1
    base+=1
nL=list(filter(lambda x:x>=2,nL))
print("\n".join(map(str,nL)))