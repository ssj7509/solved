S,st,f=input(),[],lambda t:(t[-4],t[-3],t[-2],t[-1])
for c in S:
    st.append(c)
    if len(st)>3 and f(st)==('P','P','A','P'):
        for _ in range(4):
            st.pop()
        st.append('P')
print(('NP','PPAP')[''.join(st)=='P'])