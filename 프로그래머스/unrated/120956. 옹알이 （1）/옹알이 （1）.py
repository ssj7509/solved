def solution(babbling):
    S={"aya","ye","woo","ma"}
    r=0
    for b in babbling:
        s=S.copy()
        while b and s:
            ck=1
            for t in s:
                if len(b)<len(t):continue
                tt=b[:len(t)]
                if tt in s:
                    b=b[len(t):]
                    s.remove(tt)
                    ck=0
                    break
            if ck:
                break
        if not b:
            r+=1
    return r