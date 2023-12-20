import sys
L=[]
for i in range(int(input())):
    n=int(sys.stdin.readline())
    if n==0:
        L.pop()
    else:
        L.append(n)
print(sum(L))