def distance(x1,y1,x2,y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5
testN=int(input())
for i in range(testN):
    count=0
    xyL=list(map(int,input().split()))
    caseN=int(input())
    numL=[]
    for j in range(caseN):
        numL.append(list(map(int,input().split())))
    for j in range(caseN):
        distance1=distance(numL[j][0],numL[j][1],xyL[0],xyL[1])
        distance2=distance(numL[j][0],numL[j][1],xyL[2],xyL[3])
        r=numL[j][2]
        if (distance1<r and distance2>r) or (distance1>r and distance2<r):
            count+=1   
    print(count)
