N=int(input(""))
value=0; result=0
for i in range((N//3)+1):
  tn=(N-3*i)%5
  if tn==0:
    result=i+(N-3*i)//5; value=1
    break
if value==0:
  result=-1
print(result)