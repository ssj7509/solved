s=input()+' ';d={}
for x in ('c=','c-','d-','lj','nj','s=','z=','dz='):d[x]=1
c,i=0,0
while i+c<len(s)-2:
    t=i+c
    if d.get(s[t:t+3]):
        c+=2
    elif d.get(s[t:t+2]):
        c+=1
    i+=1
print(len(s)-c-1)

