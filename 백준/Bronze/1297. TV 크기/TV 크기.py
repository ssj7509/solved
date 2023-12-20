d,h,w=map(int,input().split())
t=d**2/(h**2+w**2)
print("%d %d"%((t*h**2)**0.5//1,(t*w**2)**0.5//1))