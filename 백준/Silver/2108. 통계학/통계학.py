import sys
def f(n):
    global maxf
    if n in fD:
        fD[n]+=1
    else:
        fD[n]=1
    if fD[n]>maxf:
        maxf=fD[n]
    return n

fD={}
maxf=0
nL=sorted(map(lambda x:f(int(sys.stdin.readline())),range(int(input()))))
fL=sorted(filter(lambda x:fD[x]==maxf,fD.keys()))

print(round(sum(nL)/len(nL)))
print(nL[len(nL)//2])
print(fL[len(fL)>1])
print(nL[-1]-nL[0])
