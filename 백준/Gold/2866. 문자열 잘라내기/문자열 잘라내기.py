import sys
inp=sys.stdin.readline
r,c=map(int,inp().split())
L,cnt=['']*c,0
for i in range(r):
    s=inp()
    for j in range(len(s)-1):
        L[j]+=s[j]
for i in range(r-1):
    t=set(x[i+1:]for x in L)
    if len(t)<c:
        break
    cnt+=1
print(cnt)
