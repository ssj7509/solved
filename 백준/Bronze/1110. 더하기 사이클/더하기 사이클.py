f=lambda N:str(int(N[-1]+str(sum(map(int,list(N))))[-1]))
N=input()
T,c=f(N),1
while N!=T:
    T=f(T)
    c+=1
print(c)