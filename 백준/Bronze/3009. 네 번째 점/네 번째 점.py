numL=[[],[]]
for i in range(3):
    x,y=map(int,input().split())
    numL[0].append(x)
    numL[1].append(y)
resultL=[0,0]
for i in range(3):
    if numL[0].count(numL[0][i])==1:
        resultL[0]=numL[0][i]
    if numL[1].count(numL[1][i])==1:
        resultL[1]=numL[1][i]
print("%d %d"%(resultL[0],resultL[1]))
