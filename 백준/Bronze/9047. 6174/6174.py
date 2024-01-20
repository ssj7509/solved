import sys
f=sys.stdin.readline
for _ in range(int(f())):
    n,c=f().strip(),0
    while n!='6174':
        n=f"{int(''.join(sorted(n,reverse=True)))-int(''.join(sorted(n))):0<4}"
        c+=1
    print(c)