n=int(input())
p=list(range(2,n+1))
b,bi=2,0
while b<=int(n**0.5):
    while bi<len(p) and not p[bi]:bi+=1
    b=p[bi]
    for i in range(2,n//b+1):
        p[b*i-2]=0
    bi+=1
p,l,r=[x for x in p if x>0],0,0
s,cnt,t=0,0,1
while r<len(p):
    s+=t*p[r]
    cnt+=s==n
    if s>n:
        s-=p[l]
        l+=1
        t=0
    else:
        r+=1
        t=1
print(cnt)