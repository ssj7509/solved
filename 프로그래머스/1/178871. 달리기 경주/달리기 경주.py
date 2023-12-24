def solution(players, callings):
    d={}
    for i,p in enumerate(players):
        d[p]=i
    for c in callings:
        ti=d[c]
        d[c]-=1
        d[players[ti-1]]+=1
        players[ti],players[ti-1]=players[ti-1],players[ti]
    return players