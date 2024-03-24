t,r=0,0
for c in input():
    r+=t==0 and c==')'
    t+=(c=='(')-(t and c==')')
print(t+r)