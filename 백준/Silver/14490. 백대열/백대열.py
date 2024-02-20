import math as M
n,m=map(int,input().split(':'))
t=M.gcd(n,m)
print(f"{n//t}:{m//t}")