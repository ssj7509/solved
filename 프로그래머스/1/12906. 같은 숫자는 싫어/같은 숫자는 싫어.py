def solution(arr):
    t=arr[0]
    r=[t]
    for n in arr:
        if n!=t:
            r.append(n)
            t=n
    return r