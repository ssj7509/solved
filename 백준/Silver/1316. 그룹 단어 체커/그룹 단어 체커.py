count=0
for i in range(int(input())):
    tL=[]
    tc=''
    count+=1
    for c in input():
        if c!=tc and c in tL:
            count-=1
            break
        tL.append(c)
        tc=c
print(count)