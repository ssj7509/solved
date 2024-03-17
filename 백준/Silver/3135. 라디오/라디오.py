A,B,N,m=*map(int,input().split()+[input()]),1000
for _ in range(N):
    n=int(input())
    m=min(m,abs(B-n)+1,abs(n-B)+1)
print(min(m,abs(A-B),abs(B-A)))