def f(s):
    r=0
    for c in s:
        r+=int(c)
    return r
X=input()
count=1
while True:
    X=f(str(X))
    if X<10:
        print((count,count-1)[count==1])
        print(("NO","YES")[X%3==0])
        break
    count+=1
