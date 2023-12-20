def ftr(n1,n2):
    result=n1
    for i in range(n2-1):
        result*=n1-i-1
    return result
def C(n1,n2):
    if n1<=n2 or n2==0:return 1
    return ftr(n1,n2)//ftr(n2,n2)
N,K=map(int,input().split())
tn=min(N,K)
result=0
for i in range(tn):
    result+=C(N-1,tn-i-1)*C(K,i if N>=K else K-N+i)
print(result%1000000000)