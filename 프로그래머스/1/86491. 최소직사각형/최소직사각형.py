def solution(sizes):
    mxx,mxy=sizes[0]
    for s in sizes:
        x,y=s
        tx1,ty1=max(mxx,x),max(mxy,y)
        tx2,ty2=max(mxx,y),max(mxy,x)
        mxx,mxy=((tx1,ty1),(tx2,ty2))[tx1*ty1>tx2*ty2]
    return mxx*mxy