N,st,r,m=int(input()),[],0,0
for n in [*map(int,input().split())]+[-1]:
    n,m=(n,m)[n<0],max(m,n)
    while st:
        if st[-1]>n:
            break
        t=st.pop()
        h=min((len(st) and st[-1]+1 or m+1)-1,n)-t
        r+=t<n and h>0 and h
    if not st or st[-1]!=n:
        st.append(n)
print(r)