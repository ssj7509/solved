import sys
f=sys.stdin.readline
print(*sorted(set(f().strip()for _ in range(int(f()))),key=lambda x:(len(x),x)),sep='\n')