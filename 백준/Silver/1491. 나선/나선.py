n,m=map(int,input().split())
q,t=divmod(min(n,m)-1,2)
print((1-t and n-1)+q*(-1)**(1-t),(1-t and m-1)+(q+t)*(-1)**(1-t))