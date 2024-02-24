V,L,t,r=((1,0),(0,1),(1,1),(1,-1)),[[0]*7 for _ in range(6)],[5]*7,'ss'
for i in range(21):
    X=[*map(int,input().split())]
    s=0
    for k in (0,1):
        x,y=X[k]-1,t[X[k]-1]
        t[X[k]-1]-=1
        L[y][x]=k+1
        for xv,yv in V:
            sx,sy,s2=x-6*xv,y-6*yv,0
            for j in range(13):
                tx,ty=sx+j*xv,sy+j*yv
                s2=0<=tx<7 and 0<=ty<6 and L[ty][tx]==k+1 and s2+1
                if s2>=4:
                    print(('sk','ji')[k],i+1)
                    quit()
print('ss')