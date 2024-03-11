f=lambda:map(int,input().split())
N,M,A,B,iL=*f(),[*f()],[*f()],[0,0]
for i in range(N+M):
    t=iL[1]<M and (iL[0]==N or A[iL[0]]>B[iL[1]])
    print((A,B)[t][iL[t]],end=' ')
    iL[t]+=1