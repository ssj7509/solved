import sys
f=sys.stdin.readline
def g(n):
    if n>=250:return 5
    elif n>=200:return 4
    elif n>=140:return 3
    elif n>=100:return 2
    elif n>=60:return 1
    return 0
L=sorted([int(f())for _ in range(int(f()))],reverse=True)[:42]
print(sum(L),sum(map(g,L)))