def solution(data, col, row_begin, row_end):
    r=0
    data.sort(key=lambda x:(x[col-1],-x[0]))
    for i in range(row_begin,row_end+1):
        r^=sum(map(lambda x:x%i,data[i-1]))
    return r