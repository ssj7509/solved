import sys
f=sys.stdin.readline
while True:
    N=int(f())
    if N==0:
        break
    L,m=[0]*N,0
    for i,n in enumerate(f().split()):
        L[i]=m
        m+=int(n)
    st=set(L)
    for i in range(N,2,-1):
        s=1
        if m%i:
            s=0
            continue
        for j in range(N):
            tn,s=L[j],1
            for k in range(1,i):
                if (tn+k*(m//i))%m not in st:
                    s=0
                    break
            if s:
                break
        if s:
            print(N-i)
            break
    if not s:
        print(-1)