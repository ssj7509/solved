def ftr(n1,n2):
    result=n1
    for i in range(n2-1):
        result*=n1-i-1
    return result
def C(n2,n1):
    if n1<=n2 or n2==0:return 1
    return ftr(n1,n2)//ftr(n2,n2)
for i in range(int(input())):
    print(C(*map(int,input().split())))
