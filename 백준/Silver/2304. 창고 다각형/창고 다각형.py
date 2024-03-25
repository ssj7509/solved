import sys
f,st,m,r=sys.stdin.readline,[],0,0
for x,y in sorted(tuple(map(int,f().split()))for _ in range(int(f()))):
    d=len(st) and x-st[-1][0]-1
    r+=y+min(m,y)*d
    if not st or st[-1][1]>y:
        st.append((x,y,d+1))
    else:
        c=d+1
        while st and st[-1][1]<=y:
            w,h,t=st.pop()
            n,c=min(m,y)-h,c+t
            r+=n>0 and n*t
        st.append((x,y,c))
    m=max(m,y)
print(r)