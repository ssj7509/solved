s,L=input(),[*[0]*3,*[1]*3,*[2]*3,*[3]*3,*[4]*3,*[5]*4,*[6]*3,*[7]*4]
print(sum(L[ord(c)-65]for c in s)+len(s)*3)