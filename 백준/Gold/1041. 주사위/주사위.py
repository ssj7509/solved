N=int(input())
nL=list(map(int,input().split()))
def minf(L):
    return min(map(lambda x:sum(map(lambda y:nL[y-1],x)),L))
min3N=minf([[1,2,3],[1,2,4],[1,3,5],[1,4,5],[2,3,6],[2,4,6],[3,5,6],[4,5,6]])
min2N=minf([[1,2],[1,3],[1,4],[1,5],[2,3],[2,4],[2,6],[3,5],[3,6],[4,5],[4,6],[5,6]])
print((sum(nL)-max(nL),min(nL)*(5*N**2-20-16*(N-2))+4*(min2N+min3N)+min2N*8*(N-2))[N>1])
