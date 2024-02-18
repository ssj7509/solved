import sys
f=sys.stdin.readline
n,m,k,r=*map(int,f().split()),0
for _ in range(n):
    s,c=[*map(int,f().strip())],0
    for t in s:
        if t:
            r+=c>=k and c-k+1
            c=0
        else:
            c+=1
    r+=c>=k and c-k+1
print(r)