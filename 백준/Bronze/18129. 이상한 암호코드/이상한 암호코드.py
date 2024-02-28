s,k=input().split()
s,k,n,r,L=s.lower(),int(k),0,'',[1]*26
t=s[0]
for c in s:
    if t==c:
        n+=1
    else:
        i=ord(t)-97
        if L[i]:
            r+=('0','1')[n>=k]
        n,L[i]=1,0
    t=c
if L[ord(t)-97]:
    r+=('0','1')[n>=k]
print(r)