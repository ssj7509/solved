V,L,t=((1,0),(0,1),(1,1),(1,-1)),[[0]*7 for _ in [0]*6],[5]*7
for i in range(21):
    X=[*map(int,input().split())]
    for k in (0,1):
        x,y=X[k]-1,t[X[k]-1];t[X[k]-1]-=1;L[y][x]=k+1
        for a,b in V:
            c,d=x-6*a,y-6*b
            for j in range(10):
                e,f=c+j*a,d+j*b;s=0<=e<7 and 0<=f<6 and L[f][e]==k+1 and s+1
                if s>=4:
                    print(('sk','ji')[k],i+1);quit()
print('ss')