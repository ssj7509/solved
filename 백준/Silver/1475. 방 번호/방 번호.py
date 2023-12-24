nL,cL=[*map(int,input())],[0]*9
for n in nL:
    cL[(6,n)[n<9]]+=1
cL[6]=cL[6]//2+cL[6]%2
print(max(cL))