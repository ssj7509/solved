import sys
f,d=sys.stdin.readline,{'(':1,')':-1,'[':2,']':-2}
while True:
    s,st,r=f(),[],1
    if s=='.\n':
        break
    for c in s:
        if c not in d:
            continue
        n=d[c]
        if n>0:
            st.append(n)
        else:
            if not st or st[-1]!=-n:
                r=0
                break
            st.pop()
    print(('no','yes')[not st and r])