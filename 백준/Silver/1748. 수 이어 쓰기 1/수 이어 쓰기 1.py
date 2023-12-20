import sys
import math

N=int(sys.stdin.readline())
logn=int(math.log10(N))

print(int(((9*logn-1)*10**logn+1)/9)+(logn+1)*(N-10**logn+1))

