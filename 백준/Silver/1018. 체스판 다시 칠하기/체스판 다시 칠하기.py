N,M=map(int,input().split())
RL=[]
L=[list(map(lambda x:x=="B",input())) for x in range(N)]
for i in range(N-7):
    for j in range(M-7):
        tR=0
        for i2 in range(8):
            for j2 in range(8):
                tR+=1-((i+i2)%2^(j+j2)%2)==L[i+i2][j+j2]
        RL.append(min(tR,64-tR))
print(min(RL))
