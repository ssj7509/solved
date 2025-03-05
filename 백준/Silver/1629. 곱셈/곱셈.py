a,b,c=map(int,input().split())
t,r=a,+(a%c>0)
for n in map(int,bin(b)[:1:-1]):
    r=r*(t*n or 1)%c
    t=t*t%c
print(r)