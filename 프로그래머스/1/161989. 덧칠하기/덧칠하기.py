def solution(n, m, section):
    i=section[0]+m-1
    si,count=0,1
    while i<=section[-1]-1:
        count+=1
        while section[si]-1<i:si+=1
        i=section[si]+m-1
    return count