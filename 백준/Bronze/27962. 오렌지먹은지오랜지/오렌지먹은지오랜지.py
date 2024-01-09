n,s=int(input()),input()
for i in range(1,n+1):
    s1,s2,c=s[:i],s[-i:],0
    for j in range(i):
        c+=s1[j]==s2[j]
    if c==i-1:
        print("YES")
        quit()
print("NO")