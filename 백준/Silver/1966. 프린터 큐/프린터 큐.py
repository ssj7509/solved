n=int(input())
for i in range(n):
	dn,di=map(int,input().split())
	dL=list(map(int,input().split()))
	diL=[x for x in range(dn)]
	count=1
	while len(dL)>0:
		if dL[0]==max(dL):
			if diL[0]==di:
				print(count)
				break
			dL.pop(0); diL.pop(0)
			count+=1
		else:
			dL.append(dL.pop(0))
			diL.append(diL.pop(0))