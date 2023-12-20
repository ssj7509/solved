N=int(input())
L1=sorted(list(map(int,input().split())))
L2=reversed(sorted(list(map(int,input().split()))))
print(sum(map(lambda x,y:x*y,L1,L2)))