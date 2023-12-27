def solution(nums):
    d={}
    for n in nums:
        if d.get(n):d[n]+=1
        else:d[n]=1
    answer=min(len(d),len(nums)//2)
    return answer