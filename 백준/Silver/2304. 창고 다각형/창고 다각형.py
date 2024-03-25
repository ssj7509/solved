import sys
f,st,m,r=sys.stdin.readline,[],0,0
for x,y in sorted([*map(int,f().split())]for _ in range(int(f()))):
    c,d=len(st) and x-st[-1][0],min(m,y)
    r+=y+d*(c-1)
    if not st or st[-1][1]>y:
        st.append((x,y,c))
    else:
        while st and st[-1][1]<=y:
            w,h,t=st.pop()
            n,c=d-h,c+t
            r+=n>0 and n*t
        st.append((x,y,c))
    m=max(m,y)
print(r)