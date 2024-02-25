V,L,t=((1,0),(0,1),(1,1),(1,-1)),[[0]*7 for _ in range(6)],[5]*7
for i in range(21):
    X=[*map(int,input().split())]
    for k in (0,1):
        x,y=X[k]-1,t[X[k]-1]
        t[X[k]-1]-=1
        L[y][x]=k+1
        for xv,yv in V:
            sx,sy=x-6*xv,y-6*yv
            for j in range(10):
                tx,ty=sx+j*xv,sy+j*yv
                s=0<=tx<7 and 0<=ty<6 and L[ty][tx]==k+1 and s+1
                if s>=4:
                    print(('sk','ji')[k],i+1)
                    quit()
print('ss')