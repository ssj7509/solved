import sys
f=sys.stdin.readline
n,m=map(int,f().split())
S,L,s1=[0]*m,[0]*n,0
for i in range(n):
    L[i]=t=[*map(int,f().split())][1:]
    for p in t:
        S[p-1]+=1
for t in L:
    s2=1
    for p in t:
        s2*=S[p-1]-1>0
    if s2:
        s1=1
        break
print(s1)