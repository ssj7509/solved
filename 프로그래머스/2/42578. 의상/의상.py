def solution(clothes):
    d={}
    for _,c in clothes:
        if d.get(c):
            d[c]+=1
        else:
            d[c]=1
    answer=1
    for k in d:
        answer*=d[k]+1
    return answer-1