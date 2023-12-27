def solution(name, yearning, photo):
    d={}
    for i,c in enumerate(name):
        d[c]=yearning[i]
    answer = []
    for case in photo:
        s=0
        for c in case:
            s+=d[c] if d.get(c) else 0
        answer.append(s)
    return answer