def solution(brown, yellow):
    n1=brown+4
    n2=int((n1**2-16*(brown+yellow))**0.5)
    return [(n1+n2)//4,(n1-n2)//4]