N,st,m=int(input()),[0],0
for c in input():
    if len(st)==1 and c==')':
        st=[0]
    else:
        if c=='(':
            st.append(0)
        else:
            t=st.pop()
            st[-1]+=2+t
            m=max(m,st[-1])
print(m)