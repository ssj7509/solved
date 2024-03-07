import sys
f=sys.stdin.readline
for _ in range(int(f())):
    N,st=int(f()),[(1002,1)]
    D,U,s,m=[*map(int,f().split())]+[1002],[*map(int,f().split())]+[1002],0,1002
    for i in range(N+1):
        d,u=D[i],U[i]
        if d<=st[-1][0] and u>st[-1][0]:
            st.append((d,1))
        else:
            c,x=1,u>st[-1][0]
            y=(1001,d)[x]
            while st:
                if y<=st[-1][0]:
                    break
                t=st.pop()
                h=min(d,m)-t[0]
                s+=(x and h>0 and h)*t[1]
                c+=t[1]
            st.append((d,[1,c][x]))
        m=max(min(m,u),d)
    print(s)