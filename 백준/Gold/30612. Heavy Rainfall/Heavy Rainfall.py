N,L,st,r,m=int(input()),[*map(int,input().split())],[],0,0
for n in L:
    if not st or st[-1][0]>=n>0:
        st.append((n,1))
    else:
        x,c=n>0,1
        y=(100001,n)[x]
        while st:
            if st[-1][0]>=y:
                break
            t,l=st.pop()
            h=min(m,n)-t
            r+=(x and h>0 and h)*l
            c+=l
        if x:
            st.append((n,c))
    m=n>0 and max(m,n)
print(r)