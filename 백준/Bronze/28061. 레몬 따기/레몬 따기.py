N=int(input())
print(max((int(x)-N+i for i,x in enumerate(input().split()))))
