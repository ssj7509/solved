nlist=[]
def d(n):
    result=n
    for i in range(len(str(n))):
        result+=int(str(n)[i])
    return result
for i in range(10000):
    nlist.append(d(i))

for i in range(1,10001):
    if i not in nlist:
        print(i)