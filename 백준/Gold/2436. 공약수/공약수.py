def gcd(a,b):
    while b>0:
        a,b=b,a%b
    return a
a,b=map(int,input().split())
n2=n1n2=b//a
n1,s=1,1+n2
for i in range(2,int(n1n2**0.5)+1):
    t1,t2=i,n1n2//i
    if n1n2%i==0 and t1+t2<s and gcd(t1,t2)==1:
        n1,n2,s=t1,t2,t1+t2
print(n1*a,n2*a)