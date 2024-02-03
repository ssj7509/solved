import sys
f=sys.stdin.readline
for _ in range(int(f())):
    d={}
    s1=0
    nL=sorted([f().strip()for _ in range(int(f()))],key=lambda x:-len(x))
    for n in nL:
        s2,p=1,d
        for c in n:
            if c not in p:
                p[c]={}
                s2=0
            p=p[c]
        if s2:
            s1=1
    print(('YES','NO')[s1])