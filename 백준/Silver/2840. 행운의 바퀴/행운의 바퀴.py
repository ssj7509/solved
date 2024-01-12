import sys
f=lambda:sys.stdin.readline().split()
n,k=map(int,f())
L,st=['']*n,set()
i=0
for _ in range(k):
    s,c=f()
    i=(i+int(s))%n
    if (L[i] and L[i]!=c) or (not L[i] and c in st):
        print('!');quit()
    L[i]=c;st.add(c)
print(*[(L[(i-j)%n] or '?')for j in range(n)],sep='')