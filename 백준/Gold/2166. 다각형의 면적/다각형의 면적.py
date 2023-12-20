N=int(input())

posL=[]

for i in range(N):

    posL.append(list(map(int,input().split())))

xsum,ysum=0,0

posL.append(posL[0].copy())

for i in range(N):

    xsum+=posL[i][0]*posL[i+1][1]

    ysum+=posL[i+1][0]*posL[i][1]

print(round(abs(xsum-ysum)/2,1))