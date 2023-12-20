from math import *
n=int(input())
nL=[int(input()) for x in range(n)]
len_nL=len(nL)
sL,result=[],[]
for i in range(len_nL-1):
    for j in range(i+1,len_nL):
        sL.append(abs(nL[i]-nL[j]))
s=gcd(sL[0],sL[1]) if len(sL)>=2 else sL[0]
for i in range(1,len(sL)):
    s=gcd(s,sL[i])
i,maxN=2,int(s/2)
while i<maxN+1:
    if s%i==0:
        result.append(str(i))
        result.append(str(int(s/i)))
        maxN=s/i
    i+=1
result.append(str(s))
print(" ".join(map(str,sorted(list(map(int,set(result)))))))