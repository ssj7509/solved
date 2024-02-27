V,iL,nL,c=((1,0),(0,1),(1,1),(1,-1)),[0]*25,[0]*25,0
for i in range(5):
    for j,n in enumerate(map(int,input().split())):
        iL[n-1]=i,j
for i in range(5):
    for j,n in enumerate(map(int,input().split())):
        y,x=iL[n-1]
        nL[y*5+x]=1
        for xv,yv in V:
            sx,sy,s=x-4*xv,y-4*yv,0
            for k in range(9):
                tx,ty=sx+k*xv,sy+k*yv
                s=0<=tx<5 and 0<=ty<5 and nL[ty*5+tx] and s+1
                if s==5:
                    c+=1
                    break
        if c>2:
            print(i*5+j+1)
            quit()