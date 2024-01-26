import sys
f=lambda:int(sys.stdin.readline())
n=l=f()
t=1
n1,n2=-1,f()
L=[0,1]
r=(0,1)[n>1]
for _ in range(n-1):
    b=f()
    if b not in (n1,n2):
        n1,n2=l,b
        L[0]=t
        L[1]=1
    else:
        L[b==n2]+=1
    r=max(r,L[0],L[1])
    t=(1,t+1)[b==l]
    l=b
print(r)