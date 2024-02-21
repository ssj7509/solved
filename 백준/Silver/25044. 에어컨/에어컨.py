def f(t):
    return t+900,t+1080,t+1260
n,k=map(int,input().split())
t,s,r=0,(n+1)*1440,[]
while t<s:
    r.extend([divmod(m%1440,60) for m in f(t)if m>=n*1440 and m<s])
    t+=1440+k
print(len(r))
print(*map(lambda m:f"{m[0]:0>2}:{m[1]:0>2}",sorted(r)),sep='\n')