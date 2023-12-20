import sys
L=[[0 for j in range(100)]for i in range(100)]
for i in range(int(input())):
    a,b=map(int,sys.stdin.readline().split())
    for i in range(10):
        for j in range(10):
            L[i+a][j+b]=1
print(sum([sum(L[i])for i in range(100)]))