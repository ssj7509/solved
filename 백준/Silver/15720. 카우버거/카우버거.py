import sys
f=lambda:sorted(map(int,sys.stdin.readline().split()))
B,C,D=f()
BL,CL,DL=f(),f(),f()
p=min(B,C,D)
s=sum(BL+CL+DL)
print(s,s-sum(map(lambda L:sum(L[-p:])//10,(BL,CL,DL))),sep='\n')