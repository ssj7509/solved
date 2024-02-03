import sys
f=sys.stdin.readline
t=set('58')
for _ in range(int(f())):
    L,r=[],set()
    for _ in range(3):
        f()
        L.append([*map(int,f().split())])
    for n1 in L[0]:
        for n2 in L[1]:
            for n3 in L[2]:
                s=n1+n2+n3
                if set(str(s))<=t and s not in r:
                    r.add(s)
    print(len(r))