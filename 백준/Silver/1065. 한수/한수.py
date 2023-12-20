N=int(input(""))
count=0
if len(str(N))==1:
  count=N
else:
  for i in range(10,N+1):
    value=0; subs=int(str(i)[1])-int(str(i)[0])
    for j in range(len(str(i))-1):
      if int(str(i)[j+1])-int(str(i)[j])!=subs:
        value=1; break
    if value==0:
      count+=1
  count+=9
print(count)