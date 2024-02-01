n,m,t=map(int,input().split())
b1,b2=sorted((n,m))
L=[]
for i in range(0,t+1,b1):
    c1=i//b1
    c2=(t-i)//b2
    L.append((c1+c2,t-i-c2*b2))
print(*sorted(L,key=lambda x:(x[1],-x[0]))[0])