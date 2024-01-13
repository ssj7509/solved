import sys
f=sys.stdin.readline
print(sum(len(f())-1 for _ in range(int(f()))))