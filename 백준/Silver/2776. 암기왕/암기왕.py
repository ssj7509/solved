import sys
f=sys.stdin.readline
for _ in range(int(f())):
    _,N,_=f(),{*map(int,f().split())},f()
    for n in map(int,f().split()):
        print((n in N)+0)