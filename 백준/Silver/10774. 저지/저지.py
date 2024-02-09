import sys
f=sys.stdin.readline
n,m=map(int,(f(),f()))
t,r={'S':1,'M':2,'L':3},0
L=[t[f().strip()]for _ in range(n)]
for _ in range(m):
    c,i=f().split()
    i=int(i)-1
    if t[c]<=L[i]:
        L[i],r=0,r+1
print(r)