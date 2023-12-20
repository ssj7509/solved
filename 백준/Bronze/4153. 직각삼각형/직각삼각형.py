while True:
    numL=sorted(list(map(int,input().split())))
    if numL==[0,0,0]:
        break
    if numL[0]**2+numL[1]**2==numL[2]**2:
        print("right")
    else:
        print("wrong")
