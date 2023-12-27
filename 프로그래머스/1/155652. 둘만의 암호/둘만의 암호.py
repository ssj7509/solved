def solution(s, skip, index):
    sL=[0]*26
    for sk in skip:
        sL[ord(sk)-97]=1
    answer = ''
    for c in s:
        n=ord(c)-97
        for i in range(index):
            n=(n+1)%26
            while sL[n]:n=(n+1)%26
        answer+=chr(n+97)
    return answer