s=input().upper()
t=sorted([(x,s.count(x))for x in set(s)],key=lambda y:y[1],reverse=True)
print((t[0][0],'?')[len(t)>1 and t[0][1]==t[1][1]])