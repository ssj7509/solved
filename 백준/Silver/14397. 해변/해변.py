import sys
f,d,r,bs=sys.stdin.readline,{'.':0,'#':1},0,''
n,m=map(int,f().split())
for i in range(n):
    s,t=f().strip(),1-i%2
    for j in range(m-1):
        r+=d[s[j]]^d[s[j+1]]
    if i<1:
        bs=s
        continue
    for j in range(m):
        r+=j-t>=0 and (d[s[j]]^d[bs[j-t]])
        r+=j-t+1<m and (d[s[j]]^d[bs[j-t+1]])
    bs=s
print(r)