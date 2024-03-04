import sys
f,i=sys.stdin.readline,0
while True:
    s,i=f().strip(),i+1
    if s=='0':
        break
    while 1-len(s)%2:
        t=''.join(s[j+1]*int(s[j])for j in range(0,len(s),2))
        if s==t or sum(s[j]==s[j+2]for j in range(1,len(s)-2,2)):
            break
        s=t
    print(f"Test {i}: {s}")