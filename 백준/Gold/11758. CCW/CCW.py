import math
narr=[]
def mflr(n):
  return n-2*math.pi*math.floor(n/(2*math.pi))
for i in range(3):
  num1, num2=map(int,input("").split())
  narr.append([num1,num2])
rad1=math.atan2(narr[1][1]-narr[0][1],narr[1][0]-narr[0][0])
rad2=math.atan2(narr[2][1]-narr[1][1],narr[2][0]-narr[1][0])
tn=round(mflr(rad2-rad1),14)
if tn>0 and tn<round(math.pi,14):
  print(1)
elif tn>round(math.pi,14) and tn<round(2*math.pi,14):
  print(-1)
else:
  print(0)