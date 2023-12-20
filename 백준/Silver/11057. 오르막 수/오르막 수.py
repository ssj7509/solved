def ftr(n1,n2):
    result=n1
    for i in range(n2-1):
        result*=n1-i-1
    return result
def C(n1,n2):
    if n1<=n2 or n2==0:return 1
    return ftr(n1,n2)//ftr(n2,n2)
n=int(input())
print(C(10+n-1,n)%10007)
