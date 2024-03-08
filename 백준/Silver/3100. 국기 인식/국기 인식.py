L,R=[[*input()]for _ in range(6)],[[18]*26 for _ in range(6)]
for i in range(6):
    for j in range(9):
        n=ord(L[i][j])-65
        R[i//2][n]-=1
        R[j//3+3][n]-=1
R,m=[*map(lambda x:sorted(enumerate(x),key=lambda x:x[1]),R)],54
for i in range(3):
    for j in range(3):
        for k in range(3):
            if R[0][i][0]!=R[1][j][0] and R[1][j][0]!=R[2][k][0]:
                m=min(m,sum(r[t][1] for r,t in zip(R[:3],(i,j,k))))
            if R[3][i][0]!=R[4][j][0] and R[4][j][0]!=R[5][k][0]:
                m=min(m,sum(r[t][1] for r,t in zip(R[3:],(i,j,k))))
print(m)