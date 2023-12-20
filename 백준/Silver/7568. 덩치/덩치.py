datalist=[]; N=int(input(""))

for i in range(N):
    tlist=list(map(int,input("").split(" ")))+[0,i]
    for i in range(len(datalist)):
        if tlist[0]<datalist[i][0] and tlist[1]<datalist[i][1]:
            tlist[2]+=1
        elif tlist[0]>datalist[i][0] and tlist[1]>datalist[i][1]:
            datalist[i][2]+=1
    datalist.append(tlist)
print(datalist[0][2]+1,end='')
for i in range(N-1):
    print(' '+str(datalist[i+1][2]+1),end='')