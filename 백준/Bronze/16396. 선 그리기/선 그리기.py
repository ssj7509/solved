import sys
f=sys.stdin.readline
L=[0]*20010
for _ in range(int(f())):
    left,right=map(int,f().split())
    for i in range(left*2+1,right*2,2):
        L[i]=1
print(sum(L))