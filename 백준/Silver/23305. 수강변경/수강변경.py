N,r,iL=int(input()),0,[0,0]
L1,L2=map(lambda x:[*sorted(map(int,x.split()))],(input(),input()))
while iL[0]<N and iL[1]<N:
    if L1[iL[0]]==L2[iL[1]]:
        r+=1
        iL[0]+=1
        iL[1]+=1
    else:
        iL[L1[iL[0]]>L2[iL[1]]]+=1
print(N-r)