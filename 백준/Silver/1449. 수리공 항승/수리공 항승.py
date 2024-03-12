N,M,s,r=*map(int,input().split()),0,0
for n in sorted(map(int,input().split())):
    s=s or n
    t=n>=s+M
    s,r=(s,n)[t],r+t
print(r+(s>0))