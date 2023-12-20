num=int(input(""))
carr=[]
for i in range(num):
  minput=input("")
  marr=list(map(int,minput.split(" ")))
  d=((marr[3]-marr[0])**2+(marr[4]-marr[1])**2)**(1/2)
  if d>marr[2]+marr[5] or d<abs(marr[2]-marr[5]):
    carr.append(0)
  elif d==marr[2]+marr[5] or d==abs(marr[2]-marr[5]):
    if marr[2]==marr[5] and marr[0]==marr[3] and marr[1]==marr[4]:
      carr.append(-1)
    else:
      carr.append(1)
  elif d<marr[2]+marr[5]:
    carr.append(2)
for i in range(num):
  print(carr[i])