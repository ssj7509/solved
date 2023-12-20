def F(L,f):
    global Rstate
    if f=="R":
        Rstate*=-1
        return L
    else:
        if len(L)==0:return "error"
        else:
            del L[int(0.5*(Rstate-1))]
            return L
resultL,Rstate=[],1
caseN=int(input(""))
for i in range(caseN):
    func=input("")
    N=int(input(""))
    inputL=list(input("")[1:-1].split(','))
    if inputL==['']:inputL=[]
    for c in func:
        inputL=F(inputL,c) 
        if inputL=="error":break
    if Rstate==-1 and inputL!="error":inputL=list(reversed(inputL))
    if inputL!="error":resultL.append('['+','.join(inputL)+']')
    else:resultL.append("error")
    Rstate=1
for i in resultL:
    print(i)