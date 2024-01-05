s=input()
t1,t2="YONSEI","KOREA"
i1,i2=0,0
for c in s:
    if t1[i1]==c:i1+=1
    if i1==6:
        print(t1);break
    if t2[i2]==c:i2+=1
    if i2==5:
        print(t2);break