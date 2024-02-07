s=input()
d={'(':2,')':-2,'[':3,']':-3}
st,lvL=[],[0]
for c in s:
    n=d[c]
    if n<0 and (not st or -st[-1]!=n):
        lvL[0]=0
        break
    if n>0:
        st.append(n)
        lvL.append(0)
    else:
        t=(lvL.pop()or 1)*st.pop()
        lvL[-1]+=t
print((0,lvL[0])[not st])