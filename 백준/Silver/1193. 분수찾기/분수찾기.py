X,n=int(input()),1
def f(n):return 1+n*(n-1)//2 
while True:
    n1,n2=f(n),f(n+1)
    T=(n2-X,X-n1+1)
    if X>=n1 and X<n2:
        print(f"{T[n%2==0]}/{T[n%2==1]}")
        break
    n+=1