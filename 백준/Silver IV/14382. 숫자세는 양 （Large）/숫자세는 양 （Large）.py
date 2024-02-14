import sys
f=sys.stdin.readline
for i in range(int(f())):
    n,s,j,r=int(f()),set(),1,f"Case #{i+1}: "
    if n==0:
        print(r+"INSOMNIA")
        continue
    while True:
        t=str(n*j)
        s.update(map(int,t))
        if len(s)==10:
            print(r+t)
            break
        j+=1