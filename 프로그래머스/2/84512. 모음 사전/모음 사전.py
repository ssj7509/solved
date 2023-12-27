def solution(word):
    L=[781,156,31,6,1]
    d={'A':1,'E':2,'I':3,'O':4,'U':5}
    r=0
    for i,c in enumerate(word):
       r+=1+(d[c]-1)*L[i]
    return r
