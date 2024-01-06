import sys
f=lambda:map(int,input().split())
input();A=set(f());input();B=f()
for n in B:print(int(n in A))