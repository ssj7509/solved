N=int(input())
posL=[[0,0]]
for i in range(6):
    r,d=map(int,input().split())
    posL.append(posL[i].copy())
    posL[i+1][(r-1)//2]+=d*(-1)**(((r-1+1)%4)//2)
xsum,ysum=0,0
for i in range(6):
    xsum+=posL[i][0]*posL[i+1][1]
    ysum+=posL[i+1][0]*posL[i][1]
print(int(N*abs(xsum-ysum)/2))
