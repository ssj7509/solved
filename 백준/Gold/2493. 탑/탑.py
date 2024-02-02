from bisect import bisect_right as b
N=int(input())
L=[*map(int,input().split())]
r=[0]*N
st=[]
for i,n in enumerate(L):
    p=b(st,(-n,i+1))-1
    tn,ti=st[p]if p<len(st)and p>=0 else (0,0)
    if p<len(st):
        r[i]=ti
    for j in range(len(st)-p-1):
        st.pop()
    st.append((-n,i+1))
print(*r)