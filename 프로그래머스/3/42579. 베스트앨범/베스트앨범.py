def solution(genres, plays):
    d={}
    answer=[]
    for i,g in enumerate(genres):
        if not d.get(g):
            d[g]=[0,[]]
        d[g][0]+=plays[i]
        d[g][1].append([i,plays[i]])
    sL=sorted(d.keys(),key=lambda x:d[x][0],reverse=True)
    for k in sL:
        t=sorted(d[k][1],key=lambda x:x[1],reverse=True)[:2]
        answer+=[n[0] for n in t]
    return answer