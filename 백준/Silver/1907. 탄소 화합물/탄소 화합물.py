def f(s):
    L=[0,0,0]
    for i,c in enumerate(s):
        if c.isdigit():
            L[d[s[i-1]]]+=int(c)-1
        else:
            L[d[s[i]]]+=1
    return L
d={'C':0,'H':1,'O':2}
s1,s2=input().split('=')
L1,L2,L3=map(f,(*s1.split('+'),s2))
for i in range(1,11):
    for j in range(1,11):
        for k in range(1,11):
            t=1
            for l in range(3):
                if i*L1[l]+j*L2[l]!=k*L3[l]:
                    t=0
                    break
            if t:
                print(i,j,k)
                quit()