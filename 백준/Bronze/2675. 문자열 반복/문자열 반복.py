for i in range(int(input())):
    n,s=input().split()
    print(*(c*int(n)for c in s),sep='')
