import sys
def f(n):
    q,r=divmod(n,1)
    return int(q+(r>=0.5))
def g(L):
    if not L:
        return 0
    n=f(len(L)*0.15)
    L=sorted(L)[n:len(L)-n]
    return f(sum(L)/len(L))
inp=sys.stdin.readline
print(g([int(inp()) for _ in range(int(inp()))]))