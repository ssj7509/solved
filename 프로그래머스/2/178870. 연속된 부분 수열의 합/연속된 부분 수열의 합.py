def solution(sequence, k):
    L,l,r=[],0,0
    p,s,t=sequence,0,1
    while r<len(sequence):
        s+=t*p[r]
        if s==k:L.append([l,r])
        if s>k:
            s-=p[l]
            l+=1
            t=0
        else:
            r+=1
            t=1
    L.sort(key=lambda x:(x[1]-x[0],x[0]))
    return L[0]