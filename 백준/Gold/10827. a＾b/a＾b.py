a,b=input().split()
b=int(b)
n=len(a[a.index('.')+1:])*b
t=str(int(a.replace('.',''))**b)
print(f"{t[:-n]:0>1}.{t[-n:]:0>{(n)}}")
