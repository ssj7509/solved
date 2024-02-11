import sys
f=sys.stdin.readline
def g(L,t):
    L[t[0]],L[t[1]],L[t[2]]=L[t[1]],L[t[2]],L[t[0]]
t=((0,1,2),(0,1,3),(0,2,3),(1,2,3))
for _ in range(int(f())):
    L,s=[*map(int,f().split())],0
    L1,L2=L[:4],L[4:]
    for i in range(3):
        g(L1,t[0])
        for j in range(3):
            g(L1,t[2])
            for k in range(3):
                g(L1,t[2])
                for l in range(3):
                    g(L1,t[3])
                    if L1==L2:
                        s=1
                        break
    print(s)