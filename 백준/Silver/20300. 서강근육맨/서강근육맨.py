N,*L=map(int,[input()]+input().split())
L.sort()
print(max(*(L[i]+L[N-i-1-N%2]for i in range((N-N%2)//2)),L[-1]))