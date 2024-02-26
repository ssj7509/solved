input()
s,d,t,r=input(),{'H':0,'Y':0,'U':0},0,0
n,m=map(int,input().split())
for c in s:
    if c in d:
        d[c]+=1
        r+=min(t*n,n+m)
        t=0
    else:
        t+=1
r+=min(t*n,n+m)
print(r or 'Nalmeok',min(d.values()) or 'I love HanYang University',sep='\n')