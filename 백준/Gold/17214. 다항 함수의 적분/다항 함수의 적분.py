def f(c):
    if 'x' not in c:
        n=int(c)
        return (str(n),('','-')[n<0]+'')[abs(n)<2]+('x','')[n==0]
    n=int(c.strip('x'))//2
    return (str(n),('-','')[n>0]+'')[abs(n)<2]+'xx'
s=input().replace('-',',-').replace('+',',').lstrip(',').split(',')
t='+'.join([c for c in map(f,s)if c]+['W'])
print(t.replace('+-','-'))