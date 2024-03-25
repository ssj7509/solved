import sys
f=sys.stdin.readline
for x,y in sorted([*map(int,f().split())]for _ in range(int(f()))):
    print(x,y)