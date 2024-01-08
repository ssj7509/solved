def f(s):
    p=1
    for n in s:
        p*=int(n)
    return p
s=input()
t=1
for i in range(1,len(s)):
    if f(s[:i])==f(s[i:]):
        print("YES")
        t=0
        break
if t:
    print("NO")