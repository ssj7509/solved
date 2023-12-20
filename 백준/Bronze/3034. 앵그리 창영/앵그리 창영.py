n,w,h=map(int,input().split())
t=(w**2+h**2)**0.5
for i in range(n):
    if int(input())<=t:
        print("DA")
    else:
        print("NE")
