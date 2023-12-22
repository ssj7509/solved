import sys
inp=sys.stdin.readline
L=[0]*26
for _ in range(int(inp())):
    L[ord(inp()[0])-97]+=1
r=''.join([chr(i+97)for i,n in enumerate(L) if n>=5])
print((r,"PREDAJA")[len(r)==0])
