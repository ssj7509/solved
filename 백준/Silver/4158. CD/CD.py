import sys
f=sys.stdin.readline
while True:
    N,M=map(int,input().split())
    if not N+M:
        break
    print(len({int(f())for _ in range(N)}&{int(f())for _ in range(M)}))