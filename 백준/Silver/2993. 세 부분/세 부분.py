s=input()
r=[]
for i in range(1,len(s)-1):
    for j in range(i+1,len(s)):
        t1,t2,t3=map(lambda t:t[::-1],(s[:i],s[i:j],s[j:]))
        r.append(t1+t2+t3)
print(sorted(r)[0])