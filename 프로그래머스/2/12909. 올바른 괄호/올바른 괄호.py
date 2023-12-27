def solution(s):
    L=[0,0]
    for c in s:
        L[c==')']+=1
        if L[1]>L[0]:return False
    return L[0]==L[1]