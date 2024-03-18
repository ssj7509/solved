A,B,N,m=*map(int,input().split()+[input()]),1000
for _ in range(N):
    n=int(input())
    m=min(m,abs(B-n)+1)
print(min(m,abs(A-B)))