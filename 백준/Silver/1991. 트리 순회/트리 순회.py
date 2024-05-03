def f(L,R,d):
    l,r=L[d]
    R[0]+=chr(d+65)
    if l>=0:
        f(L,R,l)
    R[1]+=chr(d+65)
    if r>=0:
        f(L,R,r)
    R[2]+=chr(d+65)
L,R=[[-1,-1]for _ in range(26)],['']*3
for _ in range(int(input())):
    n,l,r=map(lambda x:(-1,ord(x)-65)[x>'.'],input().split())
    L[n]=[l,r]
f(L,R,0)
print(*R)