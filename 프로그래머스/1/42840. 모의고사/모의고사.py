def solution(answers):
    L=[[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    s=[0]*3
    for i,n in enumerate(answers):
        for j in range(3):
            s[j]+=n==L[j][i%len(L[j])]
    return list(filter(lambda x:s[x-1]==max(s),[1,2,3]))