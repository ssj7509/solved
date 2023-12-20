def f(L,n):
    t,k,c=L[0]+90,L[0]+n,1
    for b in L:
        if b>=k:
            k=b+n
            if b>=t:
                t=b+90
                c+=1
    return c
input()
e,o=map(lambda x:sorted([*map(int,input().split())]),range(2))
print(*map(lambda x,y:f(x,y),(e,o),(100,360)))