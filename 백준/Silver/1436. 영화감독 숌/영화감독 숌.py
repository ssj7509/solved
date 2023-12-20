def f(count):
    stack,size=1,1
    while True:
        while stack<10**size:
            s=str(stack)
            rstack=0
            rscount=''
            for j in range(size):
                if s[-(j+1)]!='6':
                    break
                rstack+=1
            if rstack>0:
                rscount=min(10**rstack-1,count)
                count-=rscount
            if count==0:
                return s[:size-rstack]+'666'+f"{rscount:0>{rstack}}"
            stack+=1
            count-=1
        size+=1
        stack=10**(size-1)

count=int(input())-1
print(666 if count==0 else f(count-1))


