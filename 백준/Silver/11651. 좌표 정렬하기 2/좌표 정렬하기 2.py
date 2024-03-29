import sys
f=sys.stdin.readline
L=sorted([[*map(int,f().split())]for _ in range(int(f()))],key=lambda x:(x[1],x[0]))
for i,j in L:
    print(i,j)