import sys
inp=sys.stdin.readline

N,M=map(int,inp().split())
nucleic_sequence=('A','G','T','C')
countL=[[0]*4 for _ in range(M)]
DNAL=[]
result=""
hamming=0

for _ in range(N):
    DNA=inp()
    DNAL.append(DNA)

    for m in range(M):
        nucleic_index=nucleic_sequence.index(DNA[m])
        countL[m][nucleic_index]+=1

for c in countL:
    max_count=max(c)
    sum_count=sum(c)
    index=sorted([i for i,n in enumerate(c) if n==max_count],key=lambda x:nucleic_sequence[x])[0]
    result+=nucleic_sequence[index]
    hamming+=sum_count-c[index]

print(result)
print(hamming)