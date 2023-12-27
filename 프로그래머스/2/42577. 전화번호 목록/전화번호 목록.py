def solution(phone_book):
    answer = True
    d={}
    for p in phone_book:
        adrr=d
        for n in p:
            if not adrr.get(n):
                adrr[n]={}
            adrr=adrr[n]
    for p in phone_book:
        adrr=d
        for n in p:
            adrr=adrr[n]
        if adrr:
            answer=False
    return answer