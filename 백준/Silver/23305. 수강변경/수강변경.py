input()
d={}
for n in map(int,input().split()):
    if n not in d:
        d[n]=0
    d[n]+=1
for n in map(int,input().split()):
    if n in d and d[n]:
        d[n]-=1
print(sum(d.values()))