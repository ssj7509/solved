a,b=map(int,input("").split())
c=int(input(""))
b+=c
a=(a+b//60)%24
b%=60
print(a,b)
