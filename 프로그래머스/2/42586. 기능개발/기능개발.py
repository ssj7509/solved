def solution(progresses, speeds):
    p=progresses
    f=lambda x:(100-p[x])//speeds[x]+((100-p[x])%speeds[x]>0)
    t1,t2,r=f(0),0,[]
    for i in range(len(p)):
        if f(i)>t1:
            r.append(t2)
            t1,t2=f(i),1
        else:
            t2+=1
    if t2>0:
        r.append(t2)
    return r