def solution(today, terms, privacies):
    td=list(map(int,today.split('.')))
    termD={}
    for s in terms:
        c,n=s.split()
        termD[c]=int(n)
    answer = []
    for i,p in enumerate(privacies):
        s,c=p.split()
        y,m,d=map(int,s.split('.'))
        if td[0]*12*28+td[1]*28+td[2]>=y*12*28+m*28+d+termD[c]*28:
            answer.append(i+1)
    return answer