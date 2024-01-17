import sys
f=sys.stdin.readline
for _ in range(int(f())):
    s=f().strip()
    L=[0]*26
    t=1
    for i in range(len(s)):
        tn=ord(s[i])-65
        L[tn]+=1
        if L[tn]==3:
            if (i==len(s)-1 or s[i]!=s[i+1]):
                print("FAKE")
                t=0
                break
            else:
                L[tn]=-1
    if t:        
        print("OK")