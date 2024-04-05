import sys
f,st=sys.stdin.readline,[]
for _ in range(int(f())):
    c,*t=map(int,f().split())
    if c==1:
        st.append(t[0])
    elif c==2:
        print(st.pop() if st else -1)
    elif c==3:
        print(len(st))
    elif c==4:
        print((not st)+0)
    else:
        print(st[-1] if st else -1)