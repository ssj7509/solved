L=[[0,0]]
for c in input():
    if c=='(':
        L.append([0,0])
    elif c==')':
        t=L.pop()
        L[-1][0]+=t[0]*L[-1][1]-1
        L[-1][1]=t[1]
    else:
        L[-1][0]+=1
        L[-1][1]=int(c)
print(L[0][0])