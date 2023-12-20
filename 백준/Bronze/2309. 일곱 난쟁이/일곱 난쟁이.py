nlist=[]; st=0
for i in range(9):
    (lambda x:nlist.append(x))(int(input("")))

tsum=sum(nlist)
for i in range(8):
    if st==1:
        break
    for j in range(i+1,9):
        if tsum-nlist[i]-nlist[j]==100:
            del nlist[i]; del nlist[j-1]; st=1
            break
nlist.sort()
for i in range(7):
    print(nlist[i])
