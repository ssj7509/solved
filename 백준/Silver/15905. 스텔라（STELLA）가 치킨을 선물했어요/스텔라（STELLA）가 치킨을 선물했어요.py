import sys
f=sys.stdin.readline
L=sorted([[*map(int,f().split())]for _ in range(int(f()))],key=lambda x:(-x[0],x[1]))
print(len([0 for n,p in L if n==L[4][0] and p>L[4][1]]))