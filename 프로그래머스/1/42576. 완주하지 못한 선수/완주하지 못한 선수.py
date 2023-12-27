def solution(participant, completion):
    d={}
    for c in completion:
        if d.get(c):d[c]+=1
        else:d[c]=1
    for p in participant:
        if not d.get(p) or d[p]==0:
            return p
        else:
            d[p]-=1