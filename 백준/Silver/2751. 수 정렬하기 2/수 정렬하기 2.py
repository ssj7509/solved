import sys
f=sys.stdin.readline
print(*sorted(int(f())for _ in range(int(f()))),sep='\n')