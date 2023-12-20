import sys
L=[]
for i in range(int(input())):
    t=sys.stdin.readline().split()
    if t[0]=="push":
        L.append(int(t[1]))
    elif t[0]=="pop":
        print(L.pop()if L else -1)
    elif t[0]=="size":
        print(len(L))
    elif t[0]=="empty":
        print(1-int(bool(L)))
    else:
        print(L[-1]if L else -1)
    
