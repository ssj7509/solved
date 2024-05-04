L,r=[[*input().split()]for _ in range(10)],0
for i in range(10):
    t1,t2,v1,v2=L[i][0],L[0][i],1,1
    for j in range(10):
        v1*=t1==L[i][j]
        v2*=t2==L[j][i]
    r+=v1+v2
print((r>0)+0)