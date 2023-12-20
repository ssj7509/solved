s,b,st=input(),list(input()),[]
for c in s:
    st.append(c)
    while st[-len(b):]==b:
        for _ in range(len(b)):st.pop()
print(('FRULA',''.join(st))[len(st)>0])