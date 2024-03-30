for p in open(0).read()[:-1].split('\n'):
    s,t,i=*p.split(),0
    for c in t:
        i+=c==s[i]
        if i==len(s):
            break
    print(('Yes','No')[i<len(s)])