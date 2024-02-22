import sys
f=sys.stdin.readline
M=[[[*map(int,f().split())]for _ in range((*map(int,f().split()),)[0])]for _ in range(int(f()))]
for i in range(len(M)-1):
    m1,m2=M[i],M[i+1]
    r1,c1,r2,c2=len(m1),len(m1[0]),len(m2),len(m2[0])
    if c1!=r2:
        print(-1)
        quit()
    M[i+1]=[[sum(m1[i][k]*m2[k][j]for k in range(c1))for j in range(c2)]for i in range(r1)]
print(sum(sum(M[-1],[]))%1000000007)