N,L=int(input()),sorted(map(int,input().split()))
print(sum(L[:N//2]),sum(L[N//2:]))