f=lambda:map(int,input().split())
a,b=f()
print(*map(lambda x:x-a*b,f()))