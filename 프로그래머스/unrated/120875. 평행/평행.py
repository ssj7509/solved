def solution(dots):
    f=lambda i,j:(dots[i][0]-dots[j][0])/(dots[i][1]-dots[j][1])
    t=((0,1,2,3),(0,2,1,3),(0,3,1,2))
    L=[f(i[0],i[1])==f(i[2],i[3])for i in t]
    
    return int(any(L))