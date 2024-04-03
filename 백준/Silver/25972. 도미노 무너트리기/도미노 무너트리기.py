import sys
f,t,r=sys.stdin.readline,0,0
for a,l in sorted(tuple(map(int,f().split()))for _ in range(int(f()))):
    r,t=r+(a>t),a+l
print(r)