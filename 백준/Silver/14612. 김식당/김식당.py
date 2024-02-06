import sys
f=sys.stdin.readline
n,m=map(int,f().split())
L=[]
for _ in range(n):
    s=f().split()
    if s[0]=="order":
        L.append(s[1:])
    elif s[0]=="sort":
        L.sort(key=lambda x:(int(x[1]),int(x[0])))
    else:
        for t in L:
            if t[0]==s[1]:
                del L[L.index(t)]
                break
    print(*((t[0]for t in L),["sleep"])[not L])