def solution(wallpaper):
    L=[]
    for i,row in enumerate(wallpaper):
        for j,c in enumerate(row):
            if c=='#':
                L.append((i,j))
    minx=maxx=L[0][1]
    miny=maxy=L[0][0]
    for xy in L:
        if xy[0]<miny:miny=xy[0]
        if xy[0]>maxy:maxy=xy[0]
        if xy[1]<minx:minx=xy[1]
        if xy[1]>maxx:maxx=xy[1]
    answer = [miny,minx,maxy+1,maxx+1]
    return answer