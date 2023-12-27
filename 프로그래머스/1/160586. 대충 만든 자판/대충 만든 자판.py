def solution(keymap, targets):
    nL=[101]*26
    for k in keymap:
        for i,c in enumerate(k):
            tn=ord(c)-65
            if i+1<nL[tn]:nL[tn]=i+1
    r=[]
    for t in targets:
        ts=0
        for c in t:
            tn=ord(c)-65
            if nL[tn]==101:
                ts=-1
                break
            ts+=nL[tn]
        r.append(ts)
    return r