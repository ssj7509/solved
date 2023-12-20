x,y,w,h=map(int,input().split())
print(min(map(abs,[x,x-w,y,y-h])))