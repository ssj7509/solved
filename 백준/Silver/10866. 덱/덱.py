import sys
L=[]
for i in range(int(input())):
    a,*b=sys.stdin.readline().split()
    if a=="push_front":
        L.insert(0,int(b[0]))
    elif a=="push_back":
        L.append(int(b[0]))
    elif a=="pop_front":
        if L:t,L=L[0],L[1:]
        else:t=-1
        print(t)
    elif a=="pop_back":
        print(L.pop()if L else -1)
    elif a=="size":
        print(len(L))
    elif a=="empty":
        print(1-bool(L))
    elif a=="front":
        print(L[0]if L else -1)
    else:
        print(L[-1]if L else -1)