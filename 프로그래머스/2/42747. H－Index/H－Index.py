def solution(citations):
    citations.sort(reverse=True)
    i,n,l=0,citations[0],len(citations)
    while n>=0:
        if i+1>=n and n>=l-i-1:
            return n
        if i<l-1 and citations[i+1]>=n-1:
            i+=1
            n=citations[i]
        else:
            n-=1