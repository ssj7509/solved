import sys
inp=sys.stdin.readline
for _ in range(int(inp())):
    s1,s2=map(lambda s:s.split()[1:],(inp(),inp()))
    A,B=map(lambda L:tuple(L.count(str(n))for n in range(1,5)),(s1,s2))
    sA,sB=sorted((A,B),key=lambda x:(x[3],x[2],x[1],x[0]))
    print((('A','B')[A is sA],'D')[A==B])