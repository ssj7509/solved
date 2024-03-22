N,*L=map(int,[input()]+input().split())
print(sum(n*(N-i)for i,n in enumerate(sorted(L))))