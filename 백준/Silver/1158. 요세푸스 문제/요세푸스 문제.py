N,K=map(int,input().split())
L=list(range(1,N+1))
i,L2=-1,[]
while L:
    i=(i+K)%N
    L2.append(str(L[i]))
    del L[i]
    N-=1;i-=1
print(f"<{', '.join(L2)}>")