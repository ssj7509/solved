a,b,v=map(int,input().split())
q,r=divmod(v-b,a-b)
print(q+(r and 1))