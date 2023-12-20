N=int(input(""))
value=0; genlist=[]
for i in range(1,N):
  tsum=0
  for j in range(len(str(i))):
    tsum+=int(str(i)[j])
  if tsum+i==N:
    genlist.append(i)
if len(genlist)==0:
  print(0)
else:
  print(min(genlist))