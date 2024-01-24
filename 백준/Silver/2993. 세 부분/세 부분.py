def f(s):
    l=len(s)
    L=list(s)
    for i in range(l//2):
        L[i],L[l-i-1]=L[l-i-1],L[i]
    return ''.join(L)
s=input()
r=[]
for i in range(1,len(s)-1):
    for j in range(i+1,len(s)):
        t1,t2,t3=map(f,(s[:i],s[i:j],s[j:]))
        r.append(t1+t2+t3)
print(sorted(r)[0])