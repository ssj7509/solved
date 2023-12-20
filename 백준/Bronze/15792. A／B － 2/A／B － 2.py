a,b=map(int,input().split())
t=str(a*10**1500//b)
tlen=len(t)
left=f"{(0,t[:tlen-1500])[tlen>1500]}"
right=f"{'0'*(1500-tlen)}{t[(0,tlen-1500)[tlen>1500]:]}".rstrip('0')
print(f"{left}.{(0,right)[len(right)>0]}")