import sys
t=("0","1","2486","3971","46","5","6","7931","8426","91")
for _ in range(int(input())):
    a,b=sys.stdin.readline().split()
    l=int(a[-1]);n=t[l]
    print((n[(int(b)-1)%len(n)],10)[l<1])