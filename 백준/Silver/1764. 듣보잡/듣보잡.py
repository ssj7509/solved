import sys
f=sys.stdin.readline
N,M=map(int,f().split())
t=sorted({f().strip()for _ in range(N)}&{f().strip()for _ in range(M)})
print(len(t),*t,sep='\n')