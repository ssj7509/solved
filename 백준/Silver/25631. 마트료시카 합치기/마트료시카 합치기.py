input()
L=[*sorted(map(int,input().split()))]
sL=[set()]
for n in L:
    i=0
    while True:
        if i==len(sL):
            sL.append(set())
        if n not in sL[i]:
            sL[i].add(n)
            break
        else:
            i+=1
print(len([st for st in sL if st]))