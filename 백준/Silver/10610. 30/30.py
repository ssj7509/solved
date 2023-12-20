n=input()
nL=sorted(list(map(int,n)),reverse=True)
if '0' not in n or sum(nL)%3!=0:
    print(-1)
else:
    print(''.join(str(i) for i in nL))
