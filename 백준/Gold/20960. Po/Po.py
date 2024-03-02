N,L,st,s=int(input()),[*map(int,input().split())]+[0],[],0
for n in L:
    while st:
        if st[-1]<n:
            break
        s+=st.pop()!=n
    st.append(n)
print(s)