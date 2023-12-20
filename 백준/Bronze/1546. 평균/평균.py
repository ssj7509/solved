num=int(input(""))
minput=input("")
marr=list(map(int,minput.split(" ")))
maxn=max(marr)
tsum=0
for i in range(num):
    tsum+=100*marr[i]/maxn
print(tsum/num)