def f(d,p,t,a):
    while t>0 and p:
        plan=p.pop()
        t-=g(d,p,t,a,plan)
def g(d,p,t,a,plan):
    mn=min(d[plan][1],t)
    d[plan][1]-=mn
    (a,p)[d[plan][1]>0].append(plan)
    return mn
def solution(plans):
    answer = []
    d={plan:[(lambda x,y:int(x)*60+int(y))(*start.split(':')),int(time)] for plan,start,time in plans}
    sL=sorted(d.keys(),key=lambda x:d[x][0])
    pause=[]
    for i in range(len(sL)-1):
        t=d[sL[i+1]][0]-d[sL[i]][0]
        t-=g(d,pause,t,answer,sL[i])
        f(d,pause,t,answer)
    answer+=[sL[-1]]+list(reversed(pause))
    return answer