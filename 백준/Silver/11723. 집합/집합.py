import sys
f,s=sys.stdin.readline,set()
for _ in range(int(f())):
    c,*n=f().split()
    if c not in ('all','empty'):
        n=int(n[0])
    if c=='add':
        s.add(n)
    elif c=='remove':
        s.discard(n)
    elif c=='check':
        print(int(n in s))
    elif c=='toggle':
        if n in s:
            s.discard(n)
        else:
            s.add(n)
    elif c=='all':
        s={*range(1,21)}
    else:
        s.clear()