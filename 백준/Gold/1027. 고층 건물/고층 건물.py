N=int(input(""))
numL=list(map(int,input("").split()))
height_L=[0]*N
for i in range(N-1):
    max_angle=0
    for j in range(i+1,N):
        angle=(numL[j]-numL[i])/(j-i)
        if j==i+1 or angle>max_angle:
            max_angle=angle
            height_L[i]+=1
            height_L[j]+=1
print(max(height_L))
