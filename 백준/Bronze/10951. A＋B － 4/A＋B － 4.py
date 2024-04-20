import sys
for p in sys.stdin:
    print(sum(map(int,p.split())))