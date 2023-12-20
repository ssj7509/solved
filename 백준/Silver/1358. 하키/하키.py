w,h,x,y,p=map(int,input().split())
incount=0
for i in range(p):
    mx,my=map(int,input().split())
    rad=h/2
    dist1=((x-mx)**2+(y+rad-my)**2)**0.5
    dist2=((x+w-mx)**2+(y+rad-my)**2)**0.5
    if (dist1<=rad and mx<=x) or (dist2<=rad and mx>=x+w):
        incount+=1
    elif mx in range(x,x+w+1) and my in range(y,y+h+1):
        incount+=1
print(incount)
