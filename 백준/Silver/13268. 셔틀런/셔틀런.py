n,i,s,p=int(input())%100,1,0,0
while n>0:
    t=(5*i,n)[n<5*i]
    p+=t*(-1)**s
    i,s,n=i+s,1-s,n-t
print((0,(p+4)//5)[p>0])