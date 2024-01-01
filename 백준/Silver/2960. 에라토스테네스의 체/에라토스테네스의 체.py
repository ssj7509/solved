N,K=map(int,input().split())
d,c,p=[0]*(N+1),0,1
while c<K:
    p+=1
    if d[p]:continue
    for i in range(p,N+1,p):
        if d[i]:continue
        c+=1;d[i]=1
        if c==K:
            print(i)
            break