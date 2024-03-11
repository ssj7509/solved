import sys
f=sys.stdin.readline
L,s=[0]*int(f()),0
for i,n in enumerate(map(int,f().split())):
    s+=n
    L[i]=s
for _ in range(int(f())):
    i,j=map(int,f().split())
    print(L[j-1]-(i-2>=0 and L[i-2]))