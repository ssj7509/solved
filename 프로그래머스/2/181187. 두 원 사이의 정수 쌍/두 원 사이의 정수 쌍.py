import math
def solution(r1, r2):
    result=0
    for i in range(r2+1):
        l=math.floor(math.sqrt(r2**2-i**2))
        r=math.ceil(math.sqrt(r1**2-i**2))if i<=r1 else 0
        result+=l-r+1
    return result*4-4*(r2-r1+1)