for i in range(int(input())):
    count=0
    for c in input():
        count+=1 if c=="(" else -1
        if count<0:break
    print("YES" if count==0 else "NO")