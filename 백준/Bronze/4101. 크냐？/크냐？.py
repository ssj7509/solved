while 1:
    n,m=map(int,input().split())
    if n+m==0:
        break
    print(('No','Yes')[n>m])