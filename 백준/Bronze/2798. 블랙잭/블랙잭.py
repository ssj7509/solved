numarr=list(map(int,input("").split()))
cardarr=list(map(int,input("").split()))
maxnum=0
for i in range(numarr[0]-2):
  for j in range(i+1,numarr[0]-1):
    for k in range(j+1,numarr[0]):
      tn=cardarr[i]+cardarr[j]+cardarr[k]
      if tn<=numarr[1] and tn>maxnum:
        maxnum=tn
print(maxnum)