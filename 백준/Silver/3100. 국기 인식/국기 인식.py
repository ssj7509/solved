L,R=[[*input()]for _ in range(6)],[[18]*26 for _ in range(6)]
for i in range(6):
    for j in range(9):
        n=ord(L[i][j])-65
        R[i//2][n]-=1
        R[j//3+3][n]-=1
R,T=[*map(lambda x:sorted(enumerate(x),key=lambda x:x[1]),R)],(0,1,2)
print(min(54,*[sum(r[t][1]for r,t in zip(tr,(i,j,k)))for tr,l in zip((R[:3],R[3:]),(0,3)) for k in T for j in T for i in T if R[0+l][i][0]!=R[1+l][j][0] and R[1+l][j][0]!=R[2+l][k][0]]))