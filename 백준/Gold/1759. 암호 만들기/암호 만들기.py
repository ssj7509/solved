def f(depth,indexL,lenN,n):
    iL=indexL.copy()
    iL[depth]=n
    tR=[]
    if depth==len(indexL)-1:
        return [iL]
    for i in range(lenN-len(indexL)-n+depth+1):
        tR+=f(depth+1,iL,lenN,n+1+i)
    return tR
def vcount(L,vL,S):
    count=0
    count2=0
    for c in L:
        if S[c] in vL:
            count+=1
        else:
            count2+=1
        if count>=1 and count2>=2:
            return True
    return False
L,C=map(int,input().split())
S=sorted(input().split())
vL=['a','e','i','o','u']
tR=[]
for i in range(C-L+1):
    tR+=f(0,[0]*L,C,i)
for c in filter(lambda x:vcount(x,vL,S),tR):
    print(''.join(map(lambda x:S[x],c)))
