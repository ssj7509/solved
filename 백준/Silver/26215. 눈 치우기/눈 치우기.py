import heapq as H
_,s,*L=input(),0,*map(lambda x:-int(x),input().split())
H.heapify(L)
while len(L)>1:
    l,r=H.heappop(L),H.heappop(L)
    t=max(l,r)
    s+=t
    for n in (n for n in (l,r) if n-t):
        H.heappush(L,n-t)
s=-(s+sum(L))
print((s,-1)[s>1440])