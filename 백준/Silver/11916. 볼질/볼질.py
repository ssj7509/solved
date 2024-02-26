input()
L,t,b,r=[*map(int,input().split())],0,0,0
for n in L:
    b+=n!=2
    if b==4 or n in (2,3):
        v=n==3 and b<4
        t=((t|(t+1))>>1<<1,t<<1)[n==3]+1-v
        b=v and b
    if t>7:
        r+=1
        t&=7
print(r)